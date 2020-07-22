"""
Tests to make sure health_metadata and add_key_to_metadata decorators function correctly
"""

from . import run_checks


TEST_COLLECTION = """
@health_metadata(('parent',{"Yes": "NAN", "True": "NAN"}),)
def check_test_collection(all_results):
    all_results["Yes"] = "NOOOO"
    all_results["True"] = "FFFFFAAALLSE"
"""


def test_create_report(testdir):
    result = run_checks(testdir, test_collection=TEST_COLLECTION)
    result.assert_outcomes(passed=1)
    assert (testdir.tmpdir / 'repo_health.yaml').exists()
