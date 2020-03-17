"""
Module to place general tests
"""
from __future__ import unicode_literals

import glob
import os

import pytest  # pylint: disable=unused-import

module_dict_key = 'repo_structure'

@pytest.fixture(scope="module")
def module_data_holder(data_holder):
    if module_dict_key not in data_holder:
        data_holder[module_dict_key] = {}
    return data_holder

def test_python_files(module_data_holder, repo_path):
    """ See if current repo has python files in it """
    python_files = glob.glob(repo_path+"/**/*.py", recursive=True)
    module_data_holder[module_dict_key]['has_python_files'] = False
    if len(python_files) > 0:
        module_data_holder[module_dict_key]['has_python_files'] = True

def test_necessary_files(module_data_holder, repo_path):
    """ Test if each repo has required files """
    necessary_files = ['openedx.yaml', 'tox.ini', 'Makefile', '.travis.yml', 'README.rst', 'pylintrc']
    for filename in necessary_files:
        if os.path.isfile(repo_path + '/' + filename):
            module_data_holder[module_dict_key][filename] = True
        else:
            module_data_holder[module_dict_key][filename] = False

def test_requirements(module_data_holder, repo_path):
    """ Test if repo has req folders and necessary .in files """
    required_req_files = ['base.in', 'dev.in', 'doc.in', 'pip-tools.in', 'quality.in', 'test.in', 'travis.in']
    module_data_holder[module_dict_key]['requirements'] = {}
    if os.path.isdir(repo_path + '/requirements'):
        module_data_holder[module_dict_key]['requirements_folder'] = True
        for filename in required_req_files:
            files = glob.glob(repo_path + "/**/" + filename, recursive=True)
            # check if any files names filename were found
            if files:
                module_data_holder[module_dict_key]['requirements'][filename] = True
    else: 
        module_data_holder[module_dict_key]['requirements_folder'] = False
        for filename in required_req_files:
            module_data_holder[module_dict_key]['requirements'][filename] = False
