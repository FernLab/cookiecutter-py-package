#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import unittest

import {{ cookiecutter.project_slug }}

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: https://doc.pytest.org/en/latest/explanation/fixtures.html
    """

def test_content(response):
    """Sample pytest test function which prints the package version."""
    assert {{ cookiecutter.project_slug }}.__version__ == "{{ cookiecutter.version }}"


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""