from __future__ import unicode_literals

import os
import re
import codecs

import pytest

module_dict_key = 'repo_structure'

def get_file_content(path):
    """
    Get the content of the UTF-8 text file at the specified path.
    Used for pytest fixtures.
    """
    if not os.path.exists(path):
        return ''
    with codecs.open(path, 'r', 'utf-8') as open_file:
        return open_file.read()

@pytest.fixture
def get_tox_ini(repo_path):
    """Fixture containing the text content of Makefile"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/tox.ini'
    return get_file_content(full_path)

@pytest.fixture(scope="module")
def module_data_holder(data_holder):
    if module_dict_key not in data_holder:
        data_holder[module_dict_key] = {}
    return data_holder


def test_has_sections(get_tox_ini, module_data_holder):
    """
    Test to check if makefile has an upgrade target
    """
    required_sections = [r'tox', r'testenv', r'testenv:quality']
    module_data_holder[module_dict_key]['has_section'] = {}
    for section in required_sections:
        regex_pattern = "\[" + section + "\]"
        match = re.search(regex_pattern, get_tox_ini)
        module_data_holder[module_dict_key]['has_section'][section] = False
        if match is not None:
             module_data_holder[module_dict_key]['has_section'][section] = True
