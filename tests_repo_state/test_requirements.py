import os

import re
import codecs

import pytest
from opynions import get_file_lines
import glob

module_dict_key = 'requires'

@pytest.fixture
def req_lines(repo_path):
    """Fixture containing the text content of req_files"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    files = glob.glob(repo_path + "/**/*.in", recursive=True)
    req_lines = []
    for file_path in files:
        lines = get_file_lines(file_path)
        req_lines.extend(lines)

    return req_lines

def test_require_django(req_lines, all_results):
    important_requirments = ["django", "pytest", "nose"]
    for req in important_requirments:
        all_results[module_dict_key][req] = False
        for line in req_lines:
            if re.search(req, line):
                all_results[module_dict_key][req] = True