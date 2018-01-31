#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

import pip
from pip.req import parse_requirements
from optparse import Option


VERSION = '0.0.4'


def parse_reqs(reqs_file):
    ''' parse the requirements '''
    options = Option('--workaround')
    options.skip_requirements_regex = None
    # Hack for old pip versions
    # Versions greater than 1.x have a required parameter "sessions" in
    # parse_requierements
    if pip.__version__.startswith('1.'):
        install_reqs = parse_requirements(reqs_file, options=options)
    else:
        from pip.download import PipSession  # pylint:disable=E0611
        options.isolated_mode = False
        install_reqs = parse_requirements(reqs_file,  # pylint:disable=E1123
                                          options=options,
                                          session=PipSession)
    return [str(ir.req) for ir in install_reqs]


BASEDIR = os.path.dirname(os.path.abspath(__file__))
REQS = parse_reqs(os.path.join(BASEDIR, 'requirements.txt'))


setup(
    name='single-cell-mooc-client',
    version=VERSION,
    author='NSE',
    author_email='',
    description='Python helper functions for single cell mooc',
    long_description='Python helper functions for single cell mooc',
    packages=find_packages(),
    install_requires=REQS,
)
