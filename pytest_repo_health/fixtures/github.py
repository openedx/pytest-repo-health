"""
Fixtures for getting information about a repository hosted on GitHub.
"""
import logging
import os
import re
from collections import namedtuple

import pytest
try:
    # github.py > 0.5.0
    from github import Client
except ImportError:
    # github.py 0.5.0
    from github import GitHub as Client
from github.errors import GitHubError

URL_PATTERN = r"github.com[/:](?P<org_name>[^/]+)/(?P<repo_name>[^/]+).git"

logger = logging.getLogger(__name__)

GITHUB_TOKEN_MISSING_ERROR_MESSAGE = "Error. No GITHUB_TOKEN environment variable found. To use any of the GitHub " \
                                     "fixtures, you must set the GITHUB_TOKEN environment variable to contain a " \
                                     "GitHub personal access token."


@pytest.fixture(scope="session")
def github_client():
    """
    A fixture to initialize a GitHub API client, using the personal access token
    obtained from the GITHUB_TOKEN environment variable.
    """
    GitHubClient = namedtuple('GitHubClient', 'object message')

    try:
        token = os.environ["GITHUB_TOKEN"]
    except KeyError:
        logger.error(GITHUB_TOKEN_MISSING_ERROR_MESSAGE)
        return GitHubClient(None, GITHUB_TOKEN_MISSING_ERROR_MESSAGE)

    return GitHubClient(Client(token), None)


@pytest.fixture
async def github_repo(git_origin_url, github_client, loop):  # pylint: disable=redefined-outer-name, unused-argument
    """
    A fixture to fetch information from the GitHub API about the examined repository.
    Because github.py uses aiohttp, any checks using this fixture must be declared
    via ``async def``.  Returns ``None`` if there is an error fetching data from
    GitHub (such as a network failure or GitHub internal error).
    """
    if git_origin_url is None:
        logger.error("Error. No origin found. There isn't an origin for this repository or directory")

    match = re.search(URL_PATTERN, git_origin_url)
    if match is None:
        logger.error("Invalid origin. Must be a GitHub origin. The origin isn't hosted on GitHub")
        return None

    org_name = match.group("org_name")
    repo_name = match.group("repo_name")
    GitHubClient = namedtuple('GitHubClient', 'object message')

    if github_client.object is None:
        logger.error(github_client.message)
        return GitHubClient(None, github_client.message)

    try:
        return GitHubClient(await github_client.object.fetch_repository(org_name, repo_name), None)
    except GitHubError as e:
        error_message = f'An error occurred while fetching the repository. GitHub API threw an error, "{e}"'
        logger.error(error_message, exc_info=e)
        return GitHubClient(None, error_message)
