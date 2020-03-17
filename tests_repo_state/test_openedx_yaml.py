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
def get_openedx_yaml(repo_path):
    """Fixture containing the text content of openedx.yaml"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/openedx.yaml'
    return get_file_content(full_path)

def test_openedx_yaml_exists(get_openedx_yaml, results_bag):
    """
    Test to check if repo has openedx.yaml file
    """
    results_bag.openedx_yaml_exists = False
    if len(get_openedx_yaml) > 0:
        results_bag.openedx_yaml_exists = True


def test_owner(get_openedx_yaml, results_bag):
    """ Test if owner line exists and get owner name """
    #TODO(jinder): decide how flexible do we want to be with this
    openedx_file = get_openedx_yaml
    regex_pattern = "(?<=owner: ).*"
    match = re.search(regex_pattern, openedx_file)
    results_bag.has_owner = False
    if  match is not None:
        results_bag.has_owner = True

        owner = match.group(0).replace("'", "")
        results_bag.owner = owner
    else:
        results_bag.owner = None
