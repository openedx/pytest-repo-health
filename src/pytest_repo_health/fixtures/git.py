"""
Fixtures for collecting data about git repositories.
"""

from pathlib import Path

from git import Repo
import pytest


@pytest.fixture(scope="session")
def git_repo(repo_path):
    """
    A fixture to fetch information about the git repository as checked out locally.
    """
    path = Path(repo_path) / '.git'
    # If there isn't a .git directory, this isn't a git repository
    if path.is_dir():
        return Repo(repo_path)
    return None


@pytest.fixture(scope="session")
def git_origin_url(git_repo):  # pylint: disable=redefined-outer-name
    """
    A fixture to fetch the URL of the online hosting for this repository.  Yields
    None if there is no origin defined for it, or if the target directory isn't
    even a git repository.
    """
    if git_repo is None:
        return None
    try:
        origin = git_repo.remotes.origin
    except ValueError:
        # This local repository isn't linked to an online origin
        return None
    return origin.url
