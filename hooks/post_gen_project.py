#!/usr/bin/env python
import pathlib


if __name__ == '__main__':

    if '{{ cookiecutter.use_precommit }}' != 'y':
        pathlib.Path('.pre-commit-config.yaml').unlink()

    if '{{ cookiecutter.create_author_file }}' != 'y':
        pathlib.Path('AUTHORS.rst').unlink()
        pathlib.Path('docs', 'authors.rst').unlink()

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        pathlib.Path('{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}_cli.py').unlink()
