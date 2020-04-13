"""
Tests to make sure pytest-repo-health plugin functions correctly
"""
import pdb

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
    testdir.runpytest()
    assert not (testdir.tmpdir / 'repo_health.yaml').exists()


def test_create_report(testdir):
    testdir.runpytest('--repo-health')
    assert (testdir.tmpdir / 'repo_health.yaml').exists()

def test_new(misc_testdir):
    tmpdir = misc_testdir.tmpdir
    testdir.runpytest('--repo-health')

    pdb.set_trace()
    pass

def check_blaw():
    pass