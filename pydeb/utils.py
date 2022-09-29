from os import makedirs, chown
from os.path import dirname, isfile

import jinja2


def simple_join(url_base: str, *paths: str):
    base = url_base
    while base.endswith("/") and paths:
        base = base[:-1]
    parts = [base]
    for path in paths:
        if not path.startswith("/"):
            path = f"/{path}"
        if path.endswith("/"):
            path = path[:-1]
        parts.append(path)

    if paths and paths[-1].endswith("/"):
        parts.append("/")

    return "".join(parts)


def create_file_if_not_exist(file_path: str, uid: int = -1, gid: int = -1):
    """Create a file and its directory if it does not exist"""
    makedirs(dirname(file_path), exist_ok=True)
    if not isfile(file_path):
        with open(file_path, "w"):
            pass
        if chown is not None:
            chown(file_path, uid, gid)


def render_template(templates_path: str, destine_file: str, root_path: str = "", **kwargs):
    """Render a template file."""
    template_loader = jinja2.FileSystemLoader(searchpath=templates_path)
    template_engine = jinja2.Environment(loader=template_loader)
    template = template_engine.get_template(destine_file, root_path)

    content = template.render(**kwargs)
    full_path = simple_join(root_path, destine_file)

    create_file_if_not_exist(full_path)

    with open(full_path, "w") as file:
        file.write(content)
