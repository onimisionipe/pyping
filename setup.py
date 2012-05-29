#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
	name='pyping',
	version='0.0.3',
	description='A pure python ICMP ping implementation using raw sockets',
	long_description=open('README.rst').read(),
	author="Geoffrey Lehée",
	author_email="geoffrey@lehee.name",
	url='https://github.com/socketubs/pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["scripts/pyping"]
)
