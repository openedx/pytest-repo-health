# pylint: disable= missing-module-docstring

import os
import re
import codecs
from setuptools import find_packages, setup

def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)



def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()
VERSION = get_version('pytest_repo_health', '__init__.py')

setup(
    name='pytest-repo-health',
    version=VERSION,
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/edX/pytest-repo-health',
    description='A pytest plugin to report on repository standards conformance',
    long_description=read('README.rst'),
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.5",
    install_requires=load_requirements('requirements/base.in'),
    zip_safe=False,
    keywords='pytest edx',
    license="Apache Software License 2.0",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'pytest11': [
            'plugin = pytest_repo_health.plugin',
        ],
    },
)
