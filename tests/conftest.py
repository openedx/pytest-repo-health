"""
conftest used to run tests on pytest-repo-health plugin
"""
import pytest
import pdb

pytest_plugins = 'pytester'


FILE = """
def check_test_collection(all_results):
    all_results["Yes"] = "NOOOO"
"""

@pytest.fixture
def misc_testdir(testdir):
    testdir.mkdir("repo_health")
    testdir.makefile('.py',**{"/repo_health/blah":FILE})
    return testdir