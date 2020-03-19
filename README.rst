===============
pytest-opynions
===============

Opynions inspects a code repository and warns the user if that repository
deviates from standards on how it should be organized.  It's
a good complement for a `cookiecutter`_; the cookiecutter provides a good
template for starting a repository with current best practices, and opynions
helps it keep up with those practices as they evolve over time.

Currently, the checks implemented in tests_repo_state are very edx specific.
Moving forward, the goal is to allow each repo checked to define their own set of checks(not yet implemented).


This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

Installation
------------

You can install "pytest-opynions" via `pip`_ from `PyPI`_::

    $ pip install pytest-opynions


Usage
-----
Once installed, following commands are used to run tests::

    $ pytest --repo-health-check True --repo-path <path of repo to be checked> --output-path <path for output report>

The above command might not work based on characteristics of your system. 

These pytest flags might help:
    -  -c <()
    -  --noconftest

At edx, the following command works for most of our repos::

    $ pytest -c <() --repo-health-check True --repo-path `pwd` --noconftest

If you would like to add custom checks for your own repo, create a dir named "repo_state_checks" and place modules with checks inside of it. 

Checks naming convention: 
    python_functions = "check_*"
    python_files = "check_*.py"

Plugin Enchancement path
-----------------

- Currently, the checks do not throw any kind of warning or error if check does not pass.
- Documenting standard reqs/checks in each check better
- create tests for this plugin(currently, you can run these checks on this repo, but no automated method for it)

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

The pull request description template should be automatically applied if you are creating a pull request from GitHub.  Otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/edx/opynions/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issues
------

The issue report template should be automatically applied if you are creating an issue on GitHub as well.  Otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/edx/opynions/blob/master/.github/ISSUE_TEMPLATE.md>`_


If you encounter any problems, please `file an issue`_ along with a detailed description.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.


Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/jinder1s/pytest-opynions/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project

-----

.. image:: https://img.shields.io/pypi/v/pytest-opynions.svg
    :target: https://pypi.org/project/pytest-opynions
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-opynions.svg
    :target: https://pypi.org/project/pytest-opynions
    :alt: Python versions

.. image:: https://travis-ci.org/jinder1s/pytest-opynions.svg?branch=master
    :target: https://travis-ci.org/jinder1s/pytest-opynions
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/jinder1s/pytest-opynions?branch=master
    :target: https://ci.appveyor.com/project/jinder1s/pytest-opynions/branch/master
    :alt: See Build Status on AppVeyor

----
