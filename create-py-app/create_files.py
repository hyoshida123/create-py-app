import os
import pathlib


def create_dir(part, *parts):
    dir = os.path.join(part, *parts)
    dir_path = pathlib.Path(dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir


def create_file(part, *parts, content=""):
    file = os.path.join(part, *parts)
    file_path = pathlib.Path(file)
    file_path.write_text(content, encoding="utf-8")


def create_file_with_project_name(part, app_name, *parts, content=""):
    content = content.replace("$1", app_name)
    create_file(part, *parts, content=content)
