from __future__ import unicode_literals

import os
import re
import codecs
import os
import re

import pytest

def get_file_content(path):
    """
    Get the content of the UTF-8 text file at the specified path.
    Used for pytest fixtures.
    """
    if not os.path.exists(path):
        return ''
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()

@pytest.fixture
def get_makefile(repo_path):
    """Fixture containing the text content of Makefile"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/Makefile'
    return get_file_content(full_path)


def test_makefile_exists(get_makefile, results_bag):
    """
    Test to check if repo hase Makefile
    """
    results_bag.has_makefile = False
    assert len(get_makefile)>0
    results_bag.has_makefile = True

def test_has_upgrade(get_makefile, results_bag):
    """
    Test to check if makefile has an upgrade target
    """
    regex_pattern = "upgrade:"
    m = re.search(regex_pattern, get_makefile)
    results_bag.has_upgrade = False
    assert m is not None
    results_bag.has_upgrade = True
