# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


# -*- coding: utf-8 -*-
"""Version module for {{ cookiecutter.project_name }}."""

__version__ = "{{ cookiecutter.version }}"
__versionalias__ = "{% now "local" %}_01"
