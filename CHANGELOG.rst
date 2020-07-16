Change Log
----------

..
   All enhancements and patches to pytest-repo-health will be documented
   in this file.  It adheres to the structure of http://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).
   
   This project adheres to Semantic Versioning (http://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
~~~~~~~~~~

*

[1.1.0] - 2020-07-16
~~~~~~~~~~~~~~~~~~~~

Added
_____

* New fixtures that allow checks to easily fetch information about a git
  repository: ``git_repo`` and ``git_origin_url``

* New fixtures that allow checks to easily fetch information from the GitHub API
  about the repository: ``github_client`` and ``github_repo``

[1.0.0] - 2020-05-13
~~~~~~~~~~~~~~~~~~~~

Added
_____

* ``--repo-health-metadata`` option to collect metadata for each check and save it in a YAML file.

* Added the current timestamp to the output (under ``TIMESTAMP``)


[0.1.0] - 2020-04-13
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initial release.
