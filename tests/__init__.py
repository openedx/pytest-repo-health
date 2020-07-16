"""
Tests of the pytest-repo-health plugin itself (including the fixtures it provides).
"""
from pathlib import Path

PYTEST_INI = """
[pytest]
addopts = --repo-health --repo-health-path {checks_path} --repo-path {repo_path}
"""


def run_checks(testdir, repo_path=None, **kwargs):
    """
    Put the check file content for each provided kwarg key into check files under the
    specified test directory, and then run them.  Runs the checks against the root of
    this repository by default, specify repo_path to run against a different directory.

    Returns the pytester RunResult so the results can be examined.
    """
    # Must put checks in a "repo_health" subdirectory to be collected
    testdir.mkpydir("repo_health")
    checks_path = Path(str(testdir.tmpdir)) / "repo_health"
    # The testdir convenience methods for file creation only work in the base directory
    for path, content in kwargs.items():
        file_path = checks_path / "check_{}.py".format(path)
        with open(str(file_path), "w") as f:
            f.write(content)
    if repo_path is None:
        repo_path = Path(__file__).parent / ".."
    # Tell pytest where to find the checks and to run them on the real repository root
    testdir.makefile(".ini", pytest=PYTEST_INI.format(checks_path=str(checks_path),
                                                      repo_path=str(repo_path)))
    return testdir.runpytest()
