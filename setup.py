#!/usr/bin/env python

"""
cfnctl
---------------
"""

#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.
#

# setup.py classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

import os
import io
from setuptools import setup, find_packages


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

_version = "0.4.2"

console_scripts = [ 'cfnctl = cfnctl.cfnctl:main',
                   ]

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cfnctl',
    version=_version,
    url='https://github.com/stelligent/cfnctl',
    license="Apache License 2.0",
    author='Michael Neil',
    author_email='michael.neil@stelligent.com',
    description='Command line launch and management tool for AWS CloudFormation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'boto3>=1.9.59',
        'jinja2>=2.10'
    ],
    packages=find_packages(),
    keywords='aws cfn control cfnctl cloudformation stack stackset',
    entry_points=dict(console_scripts=console_scripts),
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)