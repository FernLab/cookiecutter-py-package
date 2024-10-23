Tutorial
========

This tutorial refers to this FERNLab version of cookiecutter pypackage, which is a fork of `cookiecutter`_.

To start with, you will need access to GitHub or GitLab, depending on where you want to keep your package.
If you want to publish on PyPi you need an account on `PyPI`_. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/
.. _`cookiecutter`: https://github.com/audreyfeldroy/cookiecutter-pypackage


PythonPackage
=============

This manual explains how to create a directory structure for a Python Package using the **Cookiecutter** Template from FERNLab.

Furthermore, it also explains how to create a GitLab repository for that package. So following are covered:

1. Check the pre-requirements.
2. Generate directory structure.
3. Create gitlab repository.
4. Run tests
5. Create and attach a runner to the repository.

**Note!** The following instructions are for Ubuntu 22.04.

Step 1: Checking the pre-requirements.
--------------------------------------

Before generating the template, we need the **cookiecutter** to be installed. We also need the **git** version 2.28 or later. We recommend to use mamba/miniforge
and have an active mamba environment. This can be created with ``mamba create --name cookieenv python --no-default-packages`` and then ``mamba activate cookieenv``.

1.  Cookiecutter installation

.. code-block:: bash

    mamba install cookiecutter


2.  Verifying git version

.. code-block:: bash

    git --version


3.  Updating git version if it is necessary

    - For Ubuntu users:

      .. code-block:: bash

          sudo add-apt-repository ppa:git-core/ppa
          sudo apt update
          sudo apt-get upgrade -y git

    - For Windows users:

      .. code-block:: bash

          git update-git-for-windows

Step 2: Generate a Python Package directory structure.
------------------------------------------------------

1. Clone the source code from https://github.com/FernLab/cookiecutter-py-package

   .. code-block:: bash

       git clone https://github.com/FernLab/cookiecutter-py-package.git


2. Generate the directory by setting parameters:

   .. code-block:: bash

       cookiecutter cookiecutter-py-package

You need to fill the following options:

   .. code-block:: bash

       "full_name": "YourName",
       "email": "your@mail.com",
       "github_username": "Your GitHub Name or GitLab Name/Groupname",
       "gitlab_subgroup_name": "Subgroup if any, (Can be left empty)",
       "project_name": "Name of your project. Don't use special characters",
       "project_slug": "Must not contain whitespaces",
       "project_short_description": "A short description of your package. (Can be left empty)",
       "pypi_username": "In case you want to publish on PyPi add your username",
       "version": "0.1.0",
       "use_pytest": "y",
       "add_pyup_badge": "n",
       "command_line_interface": ["Argparse", "No command-line interface"],
       "create_author_file": "y",
       "open_source_license": ["MIT", "BSD-3-Clause", "ISC", "Apache-2.0", "GPL-3.0-or-later", "EUPL-1.2", "NOASSERTION"]

Note: Depending on your project choose the appropriate License. For most of the projects it is recommended option 6), the EUPL License. Could be changed later on if necessary.

Step 3: Create gitlab repository.
---------------------------------

As git version was already updated (at step 1.1.), follow the following steps:
 * Under a sub-group create a new project by clicking in **New project**.
 * Choose **Create blank project**
 * Give a project name at your choice, however, the "project slug" should be the same as the one given to the Python package.
 * Unset the option "Initialize repository with a README" and press **Create project**.
 * Follow the instructions to **Push an existing folder**. They are summarized here:

.. code-block:: bash

    cd <project_slug>
    git init --initial-branch=main
    git remote add origin git@git.gfz-potsdam.de:<group/subgroup/project_slug>.git
    git add .
    git commit -m "Initial commit"
    git push -u origin main


Step 4: Run tests.
------------------

Local Test:
   Before pushing the codes to the GitLab repository and creating the corresponding runner, we need to do some local tests to make sure if the directory was generated successfully. To do that, the template provides some commands.

   .. code-block:: bash

        cd <project_slug>
        mamba env create -f tests/CI_docker/context/environment_<project_slug>.yml
        mamba activate <project_slug>
        pip install .
        make pytest
        make lint
        make urlcheck
        make docs


which are respectively for testing the whole package, lint style, urls, and documentation.

Step 5. Create and attach a runner to the repository.
-----------------------------------------------------

* Login to a machine where you want to have your runner, for example "machine4".
* Execute the following commands:

.. code-block:: bash

    cd /path/to/your/dockerimage/directory
    git clone https://git.gfz-potsdam.de/<group/subgroup/project_slug>.git


Once you are asked for the username and password, use your email id and the master password.

.. code-block:: bash

    cd <project_slug>/tests/CI_docker
    chmod 755 build_<project_slug>_testsuite_image.sh
    ./build_<project_slug>_testsuite_image.sh


In the above code, the group is our directory in the gitlab (here is fernlab) and the subgroup is the text comes between the group and the project_slug name.
This will start building a docker image which will be the CI runner docker image.

Once it is built it will ask for a token, it is the one under **Settings** > **CI/CD** > **Runners** > **New Project Runner**: Leave Tags empty and check ``Run untagged jobs``. Check ``lock to current project``.
Set a timeout if needed (can be left empty to use the default, can be changed later) and click on ``create runner``. Please copy the token you are getting, paste it on your console and press **Enter**.
It will then ask for a name for the runner. Follow the following nomenclature:

.. code-block:: bash

    <project_slug>_CI__v<package_version>__<example_machine>

- version: since it is the first runner the version is ``0.1.0``
- example_machine: in our example ``machine4``
- you can also add your name or a short version so people know who this runner belongs to.

Once you press enter, the runner will be listed under **Settings** > **CI/CD** > **Runners** and you should now be able to see a pipeline running.

Having trouble?
---------------

Go to our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/FernLab/cookiecutter-py-package/issues
