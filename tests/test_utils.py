"""
Tests to make sure the utils for pytest-repo-health plugins work correctly.
"""

import git

from pytest_repo_health.utils import get_repo_remote_name


def test_get_repo_remote_name_on_non_git_dir(tmpdir):
    """
    Verify that the non git directory returns None on getting origin URL through get_repo_remote_name
    """
    repo_dir = tmpdir / "target-repo"
    response = get_repo_remote_name(repo_dir)
    assert response is None


def test_get_repo_remote_name_without_origin_set(tmpdir):
    """
    Verify that the git repository without remote "origin" set returns None
    on getting origin URL through get_repo_remote_name
    """
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    response = get_repo_remote_name(repo_dir)
    assert response is None


def test_get_repo_remote_name_with_http_origin(tmpdir):
    """
    Verify that the origin URL is retrieved through get_repo_remote_name on valid git repository with origin set
    """
    url = "https://github.com/openedx/pytest-repo-health.git"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_repo_remote_name(repo_dir)
    assert response == 'pytest-repo-health'


def test_get_repo_remote_name_with_http_origin_without_git(tmpdir):
    """
    Verify that the origin URL is retrieved through get_repo_remote_name on valid git repository with origin set
    """
    url = "https://github.com/openedx/pytest-repo-health"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_repo_remote_name(repo_dir)
    assert response == 'pytest-repo-health'


def test_get_repo_remote_name_with_ssh_origin(tmpdir):
    """
    Verify that the origin URL is retrieved through get_repo_remote_name on valid git repository with origin set
    """
    url = "git@github.com:edx/pytest-repo-health.git"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_repo_remote_name(repo_dir)
    assert response == 'pytest-repo-health'


def test_get_repo_remote_name_with_ssh_origin_without_git(tmpdir):
    """
    Verify that the origin URL is retrieved through get_repo_remote_name on valid git repository with origin set
    """
    url = "git@github.com:edx/pytest-repo-health"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_repo_remote_name(repo_dir)
    assert response == 'pytest-repo-health'


def test_get_repo_remote_name_with_dot_in_name(tmpdir):
    """
    Regression test for edx/.github repo.
    """
    url = "https://github.com/openedx/.github.git"
    repo_dir = tmpdir / "target-repo"
    repo = git.Repo.init(repo_dir)
    repo.create_remote("origin", url=url)
    response = get_repo_remote_name(repo_dir)
    assert response == '.github'
