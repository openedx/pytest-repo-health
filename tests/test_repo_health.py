"""
Tests to make sure pytest-repo-health plugin functions correctly
"""

from . import run_checks


TEST_COLLECTION = """
def check_test_collection(all_results):
    all_results["Yes"] = "NOOOO"
"""


def test_arguments_in_help(testdir):
    res = testdir.runpytest('--help')
    res.stdout.fnmatch_lines_random([
        '*repo-health*',
        '*output-path*',
        '*repo-path*',
    ])


def test_no_report(testdir):
    """
    Check to make sure report is not generated without --repo-health
    """
    testdir.makepyfile(check_test_collection=TEST_COLLECTION)
    testdir.runpytest()
    assert not (testdir.tmpdir / 'repo_health.yaml').exists()


def test_create_report(testdir):
    result = run_checks(testdir, test_collection=TEST_COLLECTION)
    result.assert_outcomes(passed=1)
    assert (testdir.tmpdir / 'repo_health.yaml').exists()

def test_metadata(testdir):
    result = run_checks(testdir, metadata_path='test_metadata.yaml', test_collection=TEST_COLLECTION)
    result.assert_outcomes(passed=1)
    assert (testdir.tmpdir / 'test_metadata.yaml').exists()
