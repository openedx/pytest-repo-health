"""
Fixtures for getting information about a repository hosted on GitHub.
"""
import os
import re

import pytest
from github import GitHub
from github.errors import GitHubError

URL_PATTERN = r"github.com[/:](?P<org_name>[^/]+)/(?P<repo_name>[^/\.]+)"


@pytest.fixture(scope="session")
def github_client():
    """
    A fixture to initialize a GitHub API client, using the personal access token
    obtained from the GITHUB_TOKEN environment variable.
    """
    try:
        token = os.environ["GITHUB_TOKEN"]
    except KeyError:
        raise Exception("To use any of the GitHub fixtures, you must set the GITHUB_TOKEN environment variable "
                        "to contain a GitHub personal access token.")
    return GitHub(token)


@pytest.fixture
async def github_repo(git_origin_url, github_client, loop):  # pylint: disable=redefined-outer-name, unused-argument
    """
    A fixture to fetch information from the GitHub API about the examined repository.
    Because github.py uses aiohttp, any checks using this fixture must be declared
    via ``async def``.  Returns ``None`` if there is an error fetching data from
    GitHub (such as a network failure or GitHub internal error).
    """
    if git_origin_url is None:
        # There isn't an origin for this repository or directory
        return None
    match = re.search(URL_PATTERN, git_origin_url)
    if match is None:
        # The origin isn't hosted on GitHub (might be GitLab, Bitbucket, etc.)
        return None
    org_name = match.group("org_name")
    repo_name = match.group("repo_name")
    try:
        return await github_client.fetch_repository(org_name, repo_name)
    except GitHubError:
        return None
