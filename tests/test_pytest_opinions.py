"""
Tests to make sure pytest_opinions functions correctly
"""

import pytest
import os
import yaml


def test_arguments_in_help(testdir):
    res = testdir.runpytest('--help')
    res.stdout.fnmatch_lines_random([
        '*opynions*',
        '*output-path*',
        '*repo-path*',
    ])

def test_no_report(testdir):
    """
    Check to make sure report is not generated without --repo-health-check
    """
    testdir.runpytest()
    assert not (testdir.tmpdir / 'repo_state.yaml').exists()


def test_create_report(testdir):
    res = testdir.runpytest('--opynions')
    assert (testdir.tmpdir / 'repo_state.yaml').exists()

def test_report_content_has_required_module_keys(testdir):
    """
    eventuall this test should be removed and replaced by seperate tests for each check module
    """
    res = testdir.runpytest('--opynions')
    yaml_lines = (testdir.tmpdir / 'repo_state.yaml').read()
    output_dict = yaml.safe_load(yaml_lines)
    assert 'makefile' in output_dict.keys()
    assert 'openedx_yaml' in output_dict.keys()
    assert 'repo_structure' in output_dict.keys()
    assert 'requires' in output_dict.keys()
    assert 'tox_ini' in output_dict.keys()
