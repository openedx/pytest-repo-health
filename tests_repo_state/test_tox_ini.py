import os

import re
import codecs

import pytest
from opynions import get_file_content

module_dict_key = 'repo_structure'


@pytest.fixture
def get_tox_ini(repo_path):
    """Fixture containing the text content of Makefile"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/tox.ini'
    return get_file_content(full_path)

def test_has_sections(get_tox_ini, all_results):
    """
    Test to check if makefile has an upgrade target
    """
    required_sections = [r'tox', r'testenv', r'testenv:quality']
    all_results[module_dict_key]['has_section'] = {}
    for section in required_sections:
        regex_pattern = "\[" + section + "\]"
        match = re.search(regex_pattern, get_tox_ini)
        all_results[module_dict_key]['has_section'][section] = False
        if match is not None:
             all_results[module_dict_key]['has_section'][section] = True
