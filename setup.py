"""
Setup file for secure_cloudfront_video Django plugin.
"""

from __future__ import print_function

import os
import re

from setuptools import setup


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


VERSION = get_version('secure_cloudfront_video', '__init__.py')


setup(
    name='secure-cloudfront-video',
    version=VERSION,
    description='Open edX plugin to generate signed video URLs from Amazon Cloudfront.',
    author='eduNEXT',
    author_email='contact@edunext.co',
    packages=[
        'secure_cloudfront_video'
    ],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [
            'secure_cloudfront_video = secure_cloudfront_video.apps:SecureCloudfrontVideoConfig',
        ],
    }
)
