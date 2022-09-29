#!/usr/bin/python3
from setuptools import find_packages, setup


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    description = long_description.split('\n', 1)[0]

with open('pydeb/__init__.py', 'r') as f:
    version = list(filter(lambda l: "__version__ =" in l, f.readlines()))[0].split("\"")[1]

setup(
    name="pydeb",
    version=version,
    description=description,
    long_description=long_description,
    author="Alejandro Alfonso",
    author_email="alejandroalfonso1994@gmail.com",
    url="",
    packages=find_packages(exclude=['tests']),
    entry_points={
        "console_scripts": [
            "pydeb = pydeb.launcher:main"
        ]
    },
    install_requires=[r.strip() for r in open("requirements.txt").readlines()]
)
