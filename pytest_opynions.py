# -*- coding: utf-8 -*-

import pytest
from pytest_harvest import get_fixture_store
import os

def pytest_configure(config):
    file_dir = os.path.dirname(os.path.realpath(__file__))
    config.args.append(file_dir)
    return config


def pytest_addoption(parser):
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
    return request.config.option.repo_path

@pytest.fixture
def repo_health_check(request):
    return request.config.option.repo_health_check

def pytest_ignore_collect(path, config):
    if config.getoption("repo_health_check"):
        #TODO(jinder): name "tests_repo_state" not the best
        if "tests_repo_state" not in str(path):
            return True
    else:
        if "tests_repo_state" in str(path):
            return True

def pytest_sessionfinish(session):
    fixture_store = get_fixture_store(session)
    if 'results_bag' in fixture_store:
        results_bag = fixture_store['results_bag']
        for test_name, results in results_bag.items():
            print("    - '%s':" % test_name)
            for output_name, output_value in results.items():
                print("      - '%s': %s" % (output_name, output_value))
    #TODO(jinder): decide of output file and output it
    # results_bag contains any new info stored by tests, 
    # here I would parse through info in results bag and store it in either dict or dataframe
    # and save to file

