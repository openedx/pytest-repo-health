"""
Module to place general tests
"""
from __future__ import unicode_literals

import glob

import pytest  # pylint: disable=unused-import


@pytest.fixture(scope="module")
def module_data_holder(data_holder):
    if 'general' not in data_holder:
        data_holder['general'] = {}
    return data_holder

def test_python_files(module_data_holder, repo_path):
    """ See if current repo has python files in it """
    python_files = glob.glob(repo_path+"/**/*.py", recursive=True)
    module_data_holder['general']['has_python_files'] = False
    if len(python_files) > 0:
        module_data_holder['general']['has_python_files'] = True
