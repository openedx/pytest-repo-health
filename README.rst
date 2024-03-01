==================
pytest-repo-health
==================


.. image:: https://img.shields.io/pypi/v/pytest-repo-health.svg
    :target: https://pypi.org/project/pytest-repo-health
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-repo-health.svg
    :target: https://pypi.org/project/pytest-repo-health
    :alt: Python versions

.. image:: https://github.com/openedx/pytest-repo-health/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/openedx/pytest-repo-health/actions?query=workflow%3A%22Python+CI%22
    :alt: CI

.. image:: https://ci.appveyor.com/api/projects/status/github/edx/pytest-repo-health?branch=master
    :target: https://ci.appveyor.com/project/edx/pytest-repo-health/branch/master
    :alt: See Build Status on AppVeyor

----

pytest-repo-health adapts pytest to run repo health checks as described in
`edx-repo-health`_.  Similar to how pytest runs a number of test functions,
pytest-repo-health runs a number of repo check functions.

It inspects a code repository and outputs a report with info on whether the repository
follows standards as defined by checks.  It's
a good complement for a `cookiecutter`_; the cookiecutter provides a good
template for starting a repository with current best practices, and pytest-repo-health
helps it keep up with those practices as they evolve over time.

This `pytest`_ plugin was generated with `Cookiecutter`_ along
with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

Installation
------------

For now, you need to git clone pytest-repo-health from: ``git@github.com:edx/pytest-repo-health.git``
You can install by running ``make requirements`` and then `pip install -e .`
in a Python 3.5+ virtualenv.


Usage
-----

Once installed, use this command to run checks::

    $ pytest -c <() --noconftest --repo-health --repo-health-path <path to dir with checks> --repo-path <path to repo to check>

The -c and --noconftest options are needed to stop pytest from incorrectly reading configuration files in the repo you are checking::

    -c file: load configuration from `file` instead of trying to locate one of the implicit configuration files. Helpful if invocation dir defines "add-opts" in one of its files.

    --noconftest: Don't load any conftest.py files. Helpful in case invocation dir/repository has conftest files that change configurations or cause pytest to run unnecessary code.

Other pytest options can be used.  For example, `-k` is helpful for running a subset of checks.

The "all_results" dictionary will be written as YAML to repo_health.yaml.


Adding Custom Checks
--------------------

Any repo can host repo checks. They must be in a directory named "repo_health".

If you would like to add custom checks for your own repo, create a dir named "repo_health" and place
modules with checks inside of it.

Checks naming convention:

- python_functions = "check_*"
- python_files = "check_*.py"

Checks Discovery
----------------

Pytest will look for checks in these directories, though it will only successfully run checks in the first place it finds them:
- Dir of pytest invocation(so current dir)
- Dir where pytest-repo-health is installed
- Dir specified by --repo-health-path flag in pytest invocation


Args
----

Arguments added by plugin::

  --repo-health: this arg needs to be present for plugin to do anything

  --repo-path <dir path> : the path to dir on which to perform checks. If not preset, checks will be performed on current dir

  --repo-health-path <dir path>: path to where checks are located. If not preset, plugin will look for checks in current repo

  --output-path <file path> : path to where to save resulting checks report

  --repo-health-metadata: if this is present, plugin will collect metadata(docs) from checks. You can give filename after flag(if no filename, it defaults to metadata.yaml)

Future improvements
-------------------

- Currently, the checks do not throw any kind of warning or error if check does not pass.
- Documenting standard reqs/checks in each check better.
- Create tests for this plugin(currently, you can run these checks on this repo, but no automated method for it)

Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

This software is licensed under the terms of the AGPLv3.

Please see ``LICENSE`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/openedx/.github/blob/master/CONTRIBUTING.md>`_ for details.


The pull request description template should be automatically applied if you are creating a pull request from GitHub.  Otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/openedx/pytest-repo-health/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issues
------

The issue report template should be automatically applied if you are creating an issue on GitHub as well.  Otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/openedx/pytest-repo-health/blob/master/.github/ISSUE_TEMPLATE.md>`_


If you encounter any problems, please `file an issue`_ along with a detailed description.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@openedx.org.


Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help
.. _edx-repo-health: https://github.com/openedx/edx-repo-health
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/openedx/pytest-repo-health/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
