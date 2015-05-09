#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
readme = ''

if not os.path.exists('VERSION'):
    os.system("git describe --tags | cut -c 2- > VERSION")

version = open(os.path.join(HERE, 'VERSION')).read()[:-1]

setup(
    name='test',
    version=version,
    long_description=readme,
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    license='MIT',
    platforms='any'
)
