"""
Tests to make sure the pytest-repo-health plugin fixtures work correctly.
"""

import os

import pytest

from . import run_checks

GIT_REPO = """
def check_git_repo(git_repo):
    assert git_repo.working_tree_dir

def check_git_origin_url(git_origin_url):
    assert "/pytest-repo-health" in git_origin_url
"""

NOT_GIT_REPO = """
def check_not_git_repo(all_results, git_repo):
    assert git_repo is None

def check_git_origin_url(git_origin_url):
    assert git_origin_url is None
"""

GITHUB = """
import os
import pytest

def check_github_client(github_client):
    assert github_client.message is None
    assert github_client.object is not None

async def check_github_repo(github_repo):
    assert github_repo.object is not None
    assert github_repo.object.created_at
"""


def test_git_repo(testdir):
    """
    Verify that the git fixtures initialize correctly when running against a git checkout
    """
    result = run_checks(testdir, git_repo=GIT_REPO)
    result.assert_outcomes(passed=2)


def test_not_git_repo(testdir):
    """
    Verify that the git fixtures gracefully yield None when not running against a git checkout
    """
    result = run_checks(testdir, repo_path=str(testdir.tmpdir), not_git_repo=NOT_GIT_REPO)
    result.assert_outcomes(passed=2)


@pytest.mark.skipif("GITHUB_TOKEN" not in os.environ,
                    reason="The GITHUB_TOKEN environment must be set to use the GitHub API fixtures")
def test_github(testdir):
    """
    Verify that the GitHub fixtures initialize correctly.
    """
    result = run_checks(testdir, github=GITHUB)
    result.assert_outcomes(passed=2)
