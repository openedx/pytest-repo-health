"""
Utilities for pytest plugin
"""
import re
from pathlib import Path

from git import Repo

URL_PATTERN = r"(git@|https://)([\w\.@]+)(/|:)(?P<owner>[\w,\-,\_]+)/(?P<repo_name>[\w,\-,\_]+)(.git){0,1}((/){0,1})"


def get_git_origin(repo_path):
    """
    Returns the origin url for the repo_path provided, returns None if doesn't has a remote origin.
    """
    if repo_path is None:
        return None
    path = Path(repo_path) / '.git'
    # If there isn't a .git directory, this isn't a git repository
    if not path.is_dir():
        return None
    git_repo = Repo(repo_path)
    if git_repo is None:
        return None
    try:
        origin = git_repo.remotes.origin
    except AttributeError:
        # This local repository isn't linked to an online origin
        return None
    match = re.search(URL_PATTERN, origin.url)
    return match.group("repo_name")
