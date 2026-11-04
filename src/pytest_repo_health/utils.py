"""
Utilities for pytest plugin
"""
import re
from pathlib import Path

from git import Repo

# Assumes the last slash-separated component of the remote URL is the
# name of the repo, providing for a possible extra `.git` or an extra
# forward slash at the end. This works for Github's path structure
# (which is what we need) but should also work for various other
# remotes.
#
# Examples:
# - https://github.com/openedx/edx-platform.git
# - git@github.com:edx/edx-platform.git
URL_PATTERN = r"^(git@|https://).*/(?P<repo_name>[a-zA-Z0-9_\-.]+?)(\.git)?/?$"


def get_repo_remote_name(repo_path):
    """
    Returns the repo name from the remote url for the repo_path provided.
    Returns None if repo doesn't have a remote named 'origin'.
    Assumes repo is hosted on Github.
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
    match = re.fullmatch(URL_PATTERN, origin.url)
    return match.group("repo_name")
