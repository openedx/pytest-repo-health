"""
Tests to make sure health_metadata and add_key_to_metadata decorators function correctly
"""

from . import run_checks
import yaml


TEST_HEALTH_METADATA = """
from pytest_repo_health import health_metadata
module_dict_key = "parent"
@health_metadata([module_dict_key], {"key1": "doc1", "key2": "doc2"})
def check_decorator(all_results):
    all_results[module_dict_key]["key1"] = "NOOOO"
    all_results[module_dict_key]["key2"] = "FFFFFAAALLSE"
"""


def test_health_metadata(testdir):
    """
    Test to make sure health_metadata correctly adds docs to func's __dict__.

    and make sure the plugin outputs it correctly in yaml
    """
    result = run_checks(testdir, test_health_metadata=TEST_HEALTH_METADATA)
    result.assert_outcomes(passed=1)
    metadata_yaml_path = testdir.tmpdir / 'metadata.yaml'
    assert (metadata_yaml_path).exists()
    # converting metadata_yaml_path to str cause pathlib doesn't work will with open in python 3.5
    with open(str(metadata_yaml_path)) as y_f:
        content = yaml.load(y_f, Loader=yaml.Loader)
        # name based on kwrg input to run_checks funtion
        assert "check_test_health_metadata.py" in content.keys()
        assert "check_decorator" in content["check_test_health_metadata.py"]
        assert "output_keys" in content["check_test_health_metadata.py"]["check_decorator"]
        assert ('parent', 'key1') in content["check_test_health_metadata.py"]["check_decorator"]["output_keys"]
        assert ('parent', 'key2') in content["check_test_health_metadata.py"]["check_decorator"]["output_keys"]
        assert "doc1" == content["check_test_health_metadata.py"]["check_decorator"]["output_keys"][('parent', 'key1')]
        assert "doc2" == content["check_test_health_metadata.py"]["check_decorator"]["output_keys"][('parent', 'key2')]


TEST_ADD_KEY_TO_METADATA = """
from pytest_repo_health import add_key_to_metadata
module_dict_key = "parent"
@add_key_to_metadata((module_dict_key, "key1"))
def check_decorator(all_results):
    "doc1"
    all_results[module_dict_key]["key1"] = "NOOOO"
"""


def test_add_key_to_metadata(testdir):
    """
    Test to make sure add_key_to_metadata correctly adds docs to func's __dict__.

    and make sure the plugin outputs it correctly in yaml
    """
    result = run_checks(testdir, test_add_key_to_metadata=TEST_ADD_KEY_TO_METADATA)
    result.assert_outcomes(passed=1)
    metadata_yaml_path = testdir.tmpdir / 'metadata.yaml'
    assert (metadata_yaml_path).exists()
    # converting metadata_yaml_path to str cause pathlib doesn't work will with open in python 3.5
    with open(str(metadata_yaml_path)) as y_f:
        content = yaml.load(y_f, Loader=yaml.Loader)
        # name based on kwrg input to run_checks funtion
        assert "check_test_add_key_to_metadata.py" in content.keys()
        assert "check_decorator" in content["check_test_add_key_to_metadata.py"]
        assert "output_keys" in content["check_test_add_key_to_metadata.py"]["check_decorator"]
        assert ('parent', 'key1') in content["check_test_add_key_to_metadata.py"]["check_decorator"]["output_keys"]
        assert "doc1" == content["check_test_add_key_to_metadata.py"]["check_decorator"]["output_keys"][('parent', 'key1')]

