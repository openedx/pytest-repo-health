"""
Tests to make sure the pytest-repo-health plugin fixtures work correctly.
"""

from . import run_checks

GIT_REPO = """
def check_git_repo(git_repo):
    assert git_repo.working_tree_dir
"""

NOT_GIT_REPO = """
def check_not_git_repo(all_results, git_repo):
    assert git_repo is None
"""


def test_git_repo(testdir):
    """
    Verify that the git_repo fixture initializes correctly when running against a git checkout
    """
    result = run_checks(testdir, git_repo=GIT_REPO)
    result.assert_outcomes(passed=1)


def test_not_git_repo(testdir):
    """
    Verify that the git_repo fixture gracefully yields None when not running against a git checkout
    """
    result = run_checks(testdir, repo_path=str(testdir.tmpdir), not_git_repo=NOT_GIT_REPO)
    result.assert_outcomes(passed=1)
