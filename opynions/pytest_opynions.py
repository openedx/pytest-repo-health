# -*- coding: utf-8 -*-
"""
pytest plugin to test if specific repo follows standards
"""
import os

import pytest

import yaml
import pdb
from pathlib import Path
import py

from collections import defaultdict

session_data_holder_dict = defaultdict(dict)

@pytest.fixture(scope="session")
def all_results():
    return session_data_holder_dict

def pytest_configure(config):
    """
    pytest hook used to add pytest_opynions install dir as place for pytest to find tests
    """
    file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config.args.append(file_dir)
    # Change test prefix to check postfix
    config._inicache['python_files'] = ['check_*.py']
    config._inicache['python_functions'] = ['check_*']
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
        "--repo-health-check",
        action="store",
        dest='repo_health_check',
        default=False,
        help="if true, only repo health checks will be run"
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
    return request.config.option.repo_path

@pytest.fixture
def repo_health_check(request):
    """
    pytest fixture used to see if repo health check is being run
    if repo_health_check is set to true:
        only repo health checks will be run
    else:
        no repo health checks will be run, other tests may or may not be run
    """
    return request.config.option.repo_health_check

def pytest_ignore_collect(path, config):
    """
    pytest hook that determines if pytest looks at specific directory to collect tests
    if repo_health_check is set to true:
        only tests in test directories in this plugin are collected
    """
    # if 'opynions' in str(path):
    if config.getoption("repo_health_check"):
        #TODO(jinder): name "tests_repo_state" not the best
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
    if session.config.getoption("repo_health_check"):
        with open(session.config.getoption("output_path"), "w") as write_file:
            yaml.dump(dict(session_data_holder_dict), write_file)
