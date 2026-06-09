import os


def ensure_directory_exists(path: str):
    os.makedirs(path, exist_ok=True)


def relativize(path: str) -> str:
    return os.path.relpath(path, os.getcwd())
