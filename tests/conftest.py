"""
conftest used to run tests on pytest-repo-health plugin
"""
import pytest

pytest_plugins = 'pytester'


FILE = """
def check_test_collection(all_results):
    all_results["Yes"] = "NOOOO"
"""
