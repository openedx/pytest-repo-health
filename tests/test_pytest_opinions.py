"""
Tests to make sure pytest_opinions functions correctly
"""

import pytest
import os
import yaml


def test_arguments_in_help(misc_testdir):
    res = misc_testdir.runpytest('--help')
    res.stdout.fnmatch_lines_random([
        '*repo-health-check*',
        '*output-path*',
        '*repo-path*',
    ])

def test_no_report(misc_testdir):
    """
    Check to make sure report is not generated without --repo-health-check
    """
    misc_testdir.runpytest()
    assert not (misc_testdir.tmpdir / 'repo_state.yaml').exists()


def test_create_report(misc_testdir):
    res = misc_testdir.runpytest('--repo-health-check')
    assert (misc_testdir.tmpdir / 'repo_state.yaml').exists()

def test_report_content_has_required_module_keys(misc_testdir):
    """
    eventuall this test should be removed and replaced by seperate tests for each check module
    """
    res = misc_testdir.runpytest('--repo-health-check')
    yaml_lines = (misc_testdir.tmpdir / 'repo_state.yaml').read()
    output_dict = yaml.safe_load(yaml_lines)
    assert 'makefile' in output_dict.keys()
    assert 'openedx_yaml' in output_dict.keys()
    assert 'repo_structure' in output_dict.keys()
    assert 'requires' in output_dict.keys()
    assert 'tox_ini' in output_dict.keys()
