import argparse
import importlib
import inspect
import io
import json
import os
import re
import sys
import traceback
from dataclasses import asdict, dataclass, field, fields, is_dataclass
from typing import Any

from execute_util import Rendering, pop_renderings
from file_util import ensure_directory_exists, relativize


@dataclass(frozen=True)
class StackElement:
    path: str
    line_number: int
    function_name: str
    code: str


@dataclass
class Step:
    stack: list[StackElement]
    env: dict[str, Any]
    renderings: list[Rendering] = field(default_factory=list)
    stdout: str | None = None
    stderr: str | None = None


@dataclass(frozen=True)
class Trace:
    files: dict[str, str]
    steps: list[Step]


RUNTIME_FILES = {
    "execute.py",
    "execute_util.py",
    "file_util.py",
    "lecture_util.py",
    "reference.py",
}


def to_primitive(value: Any) -> Any:
    if isinstance(value, int | float | str | bool):
        return value
    return str(value)


def to_serializable_value(value: Any) -> Any:
    if isinstance(value, int | float | str | bool) or value is None:
        return value
    if isinstance(value, list | tuple):
        return [to_serializable_value(item) for item in value]
    if isinstance(value, dict):
        return {to_primitive(key): to_serializable_value(item) for key, item in value.items()}
    if is_dataclass(value):
        return {
            field.name: to_serializable_value(getattr(value, field.name))
            for field in fields(value)
        }
    return str(value)


def get_inspect_variables(code: str) -> list[str]:
    return [match.group(1) for match in re.finditer(r"@inspect\s+(\w+)", code)]


def collect_visible_paths(module) -> list[str]:
    root = os.getcwd()
    visible_paths = {inspect.getfile(module)}

    for directory, dirs, files in os.walk(root):
        dirs[:] = [
            item
            for item in dirs
            if item not in {".git", ".scrapy", "__pycache__", "trace-viewer", "var"}
        ]
        for filename in files:
            if not filename.endswith(".py") or filename in RUNTIME_FILES:
                continue
            visible_paths.add(os.path.join(directory, filename))

    return sorted(visible_paths)


def execute(module_name: str, inspect_all_variables: bool) -> Trace:
    steps: list[Step] = []

    real_stdout = sys.stdout
    real_stderr = sys.stderr
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()

    module = importlib.import_module(module_name)
    visible_paths = collect_visible_paths(module)
    visible_path_set = set(visible_paths)
    stepovers: list[tuple[str, int]] = []

    def get_stack() -> list[StackElement]:
        stack = []
        for item in traceback.extract_stack()[2:]:
            if item.name in {"trace_func", "local_trace_func", "get_stack"}:
                continue
            if item.filename not in visible_path_set:
                continue
            stack.append(
                StackElement(
                    path=relativize(item.filename),
                    line_number=item.lineno,
                    function_name=item.name,
                    code=item.line or "",
                )
            )
        return stack

    def trace_func(frame, event, arg):
        current_path = frame.f_code.co_filename
        if current_path not in visible_path_set:
            return trace_func
        if event == "return":
            return trace_func

        stack = get_stack()
        if not stack:
            return trace_func

        item = stack[-1]
        if "@stepover" in item.code:
            marker = (item.path, item.line_number)
            if stepovers and stepovers[-1] == marker:
                stepovers.pop()
            else:
                stepovers.append(marker)

        if any(
            step_path == ancestor.path and step_line == ancestor.line_number
            for step_path, step_line in stepovers
            for ancestor in stack[:-1]
        ):
            return trace_func

        print(f"  [{len(steps)} {os.path.basename(item.path)}:{item.line_number}] {item.code}", file=real_stdout)

        open_step = Step(stack=stack, env={}, stdout="", stderr="")
        if len(steps) == 0 or open_step.stack != steps[-1].stack:
            steps.append(open_step)
        open_step_index = len(steps) - 1

        def local_trace_func(frame, event, arg):
            if open_step_index == len(steps) - 1:
                close_step = steps[-1]
            else:
                print(
                    f"  [{len(steps)} {os.path.basename(item.path)}:{item.line_number}] {item.code}",
                    file=real_stdout,
                )
                close_step = Step(stack=stack, env={}, stdout="", stderr="")
                steps.append(close_step)

            locals_ = frame.f_locals
            variables = locals_.keys() if inspect_all_variables else get_inspect_variables(item.code)
            for variable in variables:
                if variable in locals_:
                    close_step.env[variable] = to_serializable_value(locals_[variable])
                    print(f"    env: {variable} = {close_step.env[variable]}", file=real_stdout)

            close_step.stdout = stdout_buffer.getvalue()
            close_step.stderr = stderr_buffer.getvalue()
            stdout_buffer.truncate(0)
            stdout_buffer.seek(0)
            stderr_buffer.truncate(0)
            stderr_buffer.seek(0)
            close_step.renderings = pop_renderings()

            return trace_func(frame, event, arg)

        return local_trace_func

    try:
        sys.stdout = stdout_buffer
        sys.stderr = stderr_buffer
        sys.settrace(trace_func)
        module.main()
    finally:
        sys.settrace(None)
        sys.stdout = real_stdout
        sys.stderr = real_stderr

    files = {relativize(path): open(path, encoding="utf-8").read() for path in visible_paths}
    return Trace(files=files, steps=steps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--module", help="Module(s) to execute, e.g. presentation", nargs="+", required=True)
    parser.add_argument("-o", "--output-path", default="var/traces", help="Directory to save trace JSON files")
    parser.add_argument("-I", "--inspect-all-variables", action="store_true")
    args = parser.parse_args()

    ensure_directory_exists(args.output_path)

    for module in args.module:
        module = module.replace(".py", "")
        print(f"Executing {module}...")
        trace = execute(module_name=module, inspect_all_variables=args.inspect_all_variables)
        print(f"{len(trace.steps)} steps")
        output_path = os.path.join(args.output_path, f"{module}.json")
        print(f"Saving trace to {output_path}...")
        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(asdict(trace), handle, indent=2, ensure_ascii=False)
