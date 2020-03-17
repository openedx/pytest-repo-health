# -*- coding: utf-8 -*-
""" pytest plugin to test if specific repo follows standards"""
import os

import pytest

import yaml
import pdb

session_data_holder_dict = {}

@pytest.fixture(scope="session")
def data_holder():
    return session_data_holder_dict

def pytest_configure(config):
    """ pytest hook used to add pytest_opynions install dir as place for
        pytest to find tests
    """
    file_dir = os.path.dirname(os.path.realpath(__file__))
    config.args.append(file_dir)
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

    parser.addini('HELLO', 'Dummy pytest.ini setting')
    group.addoption(
        "--repo-health-check",
        action="store",
        dest='repo_health_check',
        default=False,
        help="if true, only repo health checks will be run"
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
    pytest hook that determines in pytest looks at specific directory to collect tests
    if repo_health_check is set to true:
        only tests in test directories in this plugin are collected
    """
    if config.getoption("repo_health_check"):
        #TODO(jinder): name "tests_repo_state" not the best
        if "tests_repo_state" not in str(path):
            return True
    else:
        if "tests_repo_state" in str(path):
            return True
    return False

def pytest_sessionfinish(session):
    """
    pytest hook used to collect results for tests and put into output file
    """
    with open("repo_state.yaml", "w") as write_file:
        yaml.dump(session_data_holder_dict, write_file)
    #TODO(jinder): decide of output file and output it
    # results_bag contains any new info stored by tests,
    # here I would parse through info in results bag and store it in either dict or dataframe
    # and save to file
