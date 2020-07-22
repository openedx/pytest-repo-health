"""
Tests to make sure health_metadata and add_key_to_metadata decorators function correctly
"""

from . import run_checks
import pdb


TEST_COLLECTION = """
from pytest_repo_health import health_metadata

@health_metadata(['parent'], {"Yes": "NAN", "True": "NAN"})
def check_test_collection(all_results):
    all_results["Yes"] = "NOOOO"
    all_results["True"] = "FFFFFAAALLSE"
"""


def test_decorator(testdir):
    result = run_checks(testdir, test_collection=TEST_COLLECTION)
    print(result.stdout.str())
    result.assert_outcomes(passed=1)
    assert (testdir.tmpdir / 'repo_health.yaml').exists()
