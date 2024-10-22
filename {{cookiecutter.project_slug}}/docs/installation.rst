.. SPDX-License-Identifier: {{ cookiecutter.open_source_license }}
.. FileType: DOCUMENTATION
.. FileCopyrightText: {% now 'utc', '%Y' %}, {{ cookiecutter.full_name }} at GFZ Potsdam



{% set group = cookiecutter.gitlab_group_or_username -%}
{% set subgroup = cookiecutter.gitlab_subgroup_name -%}
{% set slug = cookiecutter.project_slug -%}
{% if subgroup -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{subgroup}}/{{slug}}.git{%- endset -%}
{% else -%}
    {%- set giturl -%}git@git.gfz-potsdam.de:{{group}}/{{slug}}.git{%- endset -%}
{% endif -%}
.. _installation:

============
Installation
============


Using Mamba (recommended)
-------------------------

Using mamba_ (latest version recommended), {{ cookiecutter.project_name }} is installed as follows:

1. Update the base environment and install system-packages

   .. code-block:: bash

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


2. Clone the {{ cookiecutter.project_name }} source code:

   .. code-block:: bash

    $ git clone {{ giturl }}
    $ cd {{ cookiecutter.project_slug }}


3. Create virtual environment for {{ cookiecutter.project_slug }} and install all dependencies from the environment_{{ cookiecutter.project_slug }}.yml file and install {{ cookiecutter.project_name }} itself:

   .. code-block:: bash

    $ mamba env create -f tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml
    $ mamba activate {{ cookiecutter.project_slug }}
    $ pip install .


This is the preferred method to install {{ cookiecutter.project_name }}, as it always installs the most recent stable release and
automatically resolves all the dependencies.


Using Anaconda or Miniconda
---------------------------

Using conda_ (latest version recommended), {{ cookiecutter.project_name }} is installed as follows:

1. Update the base environment and install system-packages:

   .. code-block:: bash

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

    $ conda activate base
    $ conda update all


2. Then clone the {{ cookiecutter.project_name }} source code:

   .. code-block:: bash

    $ git clone {{ giturl }}
    $ cd {{ cookiecutter.project_slug }}


3. Create virtual environment for {{ cookiecutter.project_slug }} and install all dependencies from the environment_{{ cookiecutter.project_slug }}.yml file and install {{ cookiecutter.project_name }} itself:

   .. code-block:: bash

    $ conda env create -f tests/CI_docker/context/environment_{{ cookiecutter.project_slug }}.yml
    $ conda activate {{ cookiecutter.project_slug }}
    $ pip install .


.. note::

    {{ cookiecutter.project_name }} has been tested with Python 3.6+., i.e., should be fully compatible to all Python versions from 3.6 onwards.


.. _pip: https://pip.pypa.io
.. _Python installation guide: https://docs.python-guide.org/starting/installation/
.. _conda: https://conda.io/docs
.. _mamba: https://github.com/mamba-org/mamba
