"""
pytest plugin to test if specific repo follows standards
"""
import os
from collections import defaultdict

import pytest

import yaml

session_data_holder_dict = defaultdict(dict)

@pytest.fixture(scope="session")
def all_results():
    return session_data_holder_dict

def pytest_configure(config):
    """
    pytest hook used to add pytest_opynions install dir as place for pytest to find tests
    """

    if config.getoption("opynions"):

        # Add path to pytest-opynions dir so pytest knows where to look for checks
        file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config.args.append(file_dir)

        # add repo path so a repo can design their own checks inside a repo_state_checks dir
        repo_path = config.getoption("repo_path")
        if repo_path is None:
            repo_path = os.getcwd()
        config.args.append(os.path.abspath(repo_path))

        # in case opynions checks are in seperate repo
        opynions_path = config.getoption("opynions_path")
        if opynions_path is not None:
            config.args.append(os.path.abspath(opynions_path))

        # Change test prefix to check
        config._inicache['python_files'] = ['check_*.py']  # pylint: disable=protected-access
        config._inicache['python_functions'] = ['check_*']  # pylint: disable=protected-access
    return config


def pytest_addoption(parser):
    """
    pytest hook used to add command line options used by this plugin
    """
    group = parser.getgroup('opynions')
    group.addoption(
        "--repo-path",
        action="store",
        dest='repo_path',
        default=None,
        help="path of repo on which to perform tests"
    )

        group.addoption(
        "--opynions-path",
        action="store",
        dest='opynions_path',
        default=None,
        help="path of repo with opynions that need to be checked on repo_path"
    )

    # Since pytest opynions modifies many pytest settings, this flag is necessary
    # to make sure pytest settings are only changed when health checks run
    group.addoption(
        "--opynions",
        action="store_true",
        dest='opynions',
        default=False,
        help="if true, only repository health checks will be run"
    )

    group.addoption(
        "--output-path",
        action="store",
        dest='output_path',
        default="repo_state.yaml",
        help="path to where yaml file should be stored"
    )


@pytest.fixture
def repo_path(request):
    """
    pytest fixture to be used to get path to repo being tested
    """
    path = request.config.option.repo_path
    if path is None:
        path = os.getcwd()
    path = os.path.abspath(path)
    return path

@pytest.fixture
def opynions(request):
    """
    pytest fixture used to see if repo health check is being run
    if opynions is set to true:
        only repo health checks will be run
    else:
        no opynions checks will be run, other tests may or may not be run
    """
    return request.config.option.opynions

def pytest_ignore_collect(path, config):
    """
    pytest hook that determines if pytest looks at specific file to collect tests
    if opynions is set to true:
        only tests in test files with "repo_state_checks" in their path will be collected
    """
    if config.getoption("opynions"):
        if "repo_state_checks" not in str(path):
            return True
    else:
        if "repo_state_checks" in str(path):
            return True
    return False

def pytest_sessionfinish(session):
    """
    pytest hook used to collect results for tests and put into output file
    """
    if session.config.getoption("opynions"):
        with open(session.config.getoption("output_path"), "w") as write_file:
            yaml.dump(dict(session_data_holder_dict), write_file)
