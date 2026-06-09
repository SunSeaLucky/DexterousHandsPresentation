import inspect
import os
import subprocess
import csv
from dataclasses import dataclass
from typing import Any

from file_util import relativize
from reference import Reference


@dataclass(frozen=True)
class CodeLocation:
    path: str
    line_number: int


@dataclass(frozen=True)
class Rendering:
    type: str
    data: Any = None
    style: dict | None = None
    external_link: Reference | None = None
    internal_link: CodeLocation | None = None


_current_renderings: list[Rendering] = []


def text(message: str, style: dict | None = None, verbatim: bool = False):
    style = style or {}
    messages = message.split("\n") if verbatim else [message]
    if verbatim:
        style = {
            "fontFamily": "monospace",
            "whiteSpace": "pre",
            **style,
        }

    for item in messages:
        _current_renderings.append(Rendering(type="markdown", data=item, style=style))


def image(url: str, style: dict | None = None, width: int | str | None = None):
    style = style or {}
    if width is not None:
        style["width"] = width

    if not url.startswith("http") and not os.path.exists(url):
        raise ValueError(f"Image not found: {url}")

    _current_renderings.append(Rendering(type="image", data=url, style=style))


def table(path: str, style: dict | None = None):
    style = style or {}
    if not os.path.exists(path):
        raise ValueError(f"Table not found: {path}")

    with open(path, newline="", encoding="utf-8-sig") as handle:
        rows = [row for row in csv.reader(handle)]

    if not rows:
        raise ValueError(f"Table is empty: {path}")

    _current_renderings.append(Rendering(type="table", data=rows, style=style))


def link(arg: type | Reference | str | None = None, style: dict | None = None, **kwargs):
    style = style or {}

    if arg is None:
        _current_renderings.append(Rendering(type="link", style=style, external_link=Reference(**kwargs)))
    elif isinstance(arg, Reference):
        _current_renderings.append(Rendering(type="link", style=style, external_link=arg))
    elif isinstance(arg, str):
        _current_renderings.append(Rendering(type="link", style=style, external_link=Reference(url=arg)))
    elif isinstance(arg, type) or callable(arg):
        path = inspect.getfile(arg)
        _, line_number = inspect.getsourcelines(arg)
        _current_renderings.append(
            Rendering(
                type="link",
                data=arg.__name__,
                style=style,
                internal_link=CodeLocation(relativize(path), line_number),
            )
        )
    else:
        raise ValueError(f"Invalid link target: {arg}")


def system_text(command: list[str]):
    output = subprocess.check_output(command).decode("utf-8")
    text(output, verbatim=True)


def pop_renderings() -> list[Rendering]:
    renderings = _current_renderings.copy()
    _current_renderings.clear()
    return renderings
