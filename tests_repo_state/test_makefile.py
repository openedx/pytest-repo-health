from __future__ import unicode_literals

import os
import re
import codecs

import pytest

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
def get_makefile(repo_path):
    """Fixture containing the text content of Makefile"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/Makefile'
    return get_file_content(full_path)

@pytest.fixture(scope="module")
def module_data_holder(data_holder):
    if 'makefile' not in data_holder:
        data_holder['makefile'] = {}
    return data_holder


def test_makefile_exists(get_makefile, module_data_holder):
    """
    Test to check if repo hase Makefile
    """
    module_data_holder['makefile']['exists'] = False
    if len(get_makefile) > 0:
        module_data_holder['makefile']['exists'] = True

def test_has_upgrade(get_makefile, module_data_holder):
    """
    Test to check if makefile has an upgrade target
    """
    regex_pattern = "upgrade:"
    match = re.search(regex_pattern, get_makefile)
    module_data_holder['makefile']['has_upgrade_target'] = False
    if match is not None:
        module_data_holder['makefile']['has_upgrade_target'] = True
