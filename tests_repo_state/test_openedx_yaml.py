from __future__ import unicode_literals

import os
import re
import codecs

import pytest
import yaml

from opynions import get_file_content
# TODO(jinder): should I implement methods relaying on openedx.yaml being parsable?
#Decision: require openedx.yaml to be parsable

module_dict_key = "openedx_yaml"

@pytest.fixture
def openedx_yaml(repo_path):
    """Fixture containing the text content of openedx.yaml"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/openedx.yaml'
    return get_file_content(full_path)

def test_yaml_parsable(openedx_yaml, all_results):
    try:
        data = yaml.load(openedx_yaml, Loader=yaml.Loader)
        all_results[module_dict_key]['is_parsable'] = bool(data)
    except:
        all_results[module_dict_key]['is_parsable'] = False

def test_owner(openedx_yaml, all_results):
    """ Test if owner line exists and get owner name """
    #TODO(jinder): decide how flexible do we want to be with this
    data = yaml.load(openedx_yaml, Loader=yaml.Loader)
    all_results[module_dict_key]['owner'] = None
    if 'owner' in data.keys():
        all_results[module_dict_key]['owner'] = data['owner']

def test_oep(openedx_yaml, all_results):
    important_oeps = [2, 7, 18, 30]
    data = yaml.load(openedx_yaml, Loader=yaml.Loader)
    if 'oeps' in data:
        oeps = data['oeps']
        for oep_num in important_oeps:
            oep_name = "oep-{num}".format(num=oep_num)
            if oep_name in oeps:
                all_results[module_dict_key][oep_name] = oeps[oep_name]
            else:
                all_results[module_dict_key][oep_name] = False

