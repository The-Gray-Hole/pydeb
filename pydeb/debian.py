from os import getcwd, walk
from os.path import dirname, realpath
from .utils import render_template, simple_join


def render_build(kwargs: dict):
    cwd = getcwd()
    templates_dir = simple_join(dirname(realpath(__file__)), "templates")
    kwargs["pydeb"]["debian-files"] = kwargs["debian-files"]

    for dirpath, dirnames, filenames in walk(templates_dir):
        for file in filenames:
            full_path = simple_join(dirpath, file)
            sub_path = full_path[len(templates_dir):]
            render_template(templates_dir, sub_path, cwd, **kwargs)
