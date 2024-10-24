.. SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
.. FileType: DOCUMENTATION
.. FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam



{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{subgroup}}/{{slug}}{%- endset -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{subgroup}}/{{slug}}.git{%- endset -%}
{% else -%}
    {%- set projecturl -%}{{ 'https://git.gfz-potsdam.de' }}/{{group}}/{{slug}}{%- endset -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{slug}}.git{%- endset -%}
{% endif -%}
.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at {{ projecturl }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitLab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitLab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at {{ projecturl }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Commit Changes
--------------

How to
~~~~~~

0. Update the base environment and install system-packages::

    $ apt-get update -y && \
       echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    $ apt-get install -y -q dialog apt-utils && \
    $ apt-get install -y -q \
          bzip2 \
          curl \
          fish \
          gcc \
          gdb \
          make \
          nano \
          python3-pip \
          tree \
          wget \
          cron \
          zip \
          unzip \
          vim \
          bash-completion \
          git \
          git-lfs && \
    $ git-lfs install

    $ mamba activate base
    $ mamba update all

1. Clone the repository::

    $ git clone {{ giturl }}

2. Create an environment::

    $ cd {{ cookiecutter.project_slug }}/
    $ mamba env create -f {{ cookiecutter.project_slug }}/tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml
    $ pip install .

3. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes, check that your changes pass flake8 and the
   tests::

    $ make pytest
    $ make lint
    $ make urlcheck


5. Commit your changes and push your branch to GitLab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push -u origin name-of-your-bugfix-or-feature

6. Submit a merge request through the GitLab website.

Sign your commits
~~~~~~~~~~~~~~~~~

Please note that our license terms only allow signed commits.
A guideline how to sign your work can be found here: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

If you are using the PyCharm IDE, the `Commit changes` dialog has an option called `Sign-off commit` to
automatically sign your work.


License header
~~~~~~~~~~~~~~

If you commit new Python files, please note that they have to contain the following license header:

.. code:: bash

    # SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
    # FileType: SOURCE
    # FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam


Merge Request Guidelines
------------------------

Before you submit a pull request, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for the latest three Python versions. Check
   {{ projecturl }}/-/merge_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_{{ cookiecutter.project_slug }} -k <test_name_prefix>

Code of Conduct
---------------

Please note that this project is released with a `Contributor Code of Conduct`_.
By participating in this project you agree to abide by its terms.

.. _`Contributor Code of Conduct`: CODE_OF_CONDUCT.rst
