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
