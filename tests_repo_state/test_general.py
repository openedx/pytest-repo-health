"""
Module to place general tests
"""
from __future__ import unicode_literals

import glob

import pytest  # pylint: disable=unused-import


def test_python_files(results_bag, repo_path):
    """ See if current repo has python files in it """
    python_files = glob.glob(repo_path+"/**/*.py", recursive=True)
    results_bag.has_python_files = False
    if len(python_files) > 0:
        results_bag.has_python_files = True
