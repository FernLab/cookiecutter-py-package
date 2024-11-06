#!/usr/bin/env python

# SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
# FileType: SOURCE
# FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
import {{ cookiecutter.project_slug }}

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: https://doc.pytest.org/en/latest/explanation/fixtures.html
    """

def test_content(response):
    """Sample pytest test function which prints the package version."""
    assert {{ cookiecutter.project_slug }}.__version__ == "{{ cookiecutter.version }}"


class Test{{ cookiecutter.project_slug|title }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

        @classmethod
    def setup_class(cls):
        """Run once for the entire class to set up any state."""
        print("Setting up Test_{{ cookiecutter.project_slug|title }} class")

    @classmethod
    def teardown_class(cls):
        """Run once after all tests in the class have run."""
        print("Tearing down Test_{{ cookiecutter.project_slug|title }} class")

    def setup_method(self, method):
        """Run before each test method to set up clean state."""
        print(f"Setting up for {method.__name__}")

    def teardown_method(self, method):
        """Run after each test method to clean up."""
        print(f"Tearing down {method.__name__}")

    def test_000_something(self):
        """Test something."""
        print({{ cookiecutter.project_slug }}.__version__)
