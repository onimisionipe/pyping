#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup

PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_authors():
	authors = []
	try:
		f = file(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r")
		for line in f:
			if not line.strip().startswith("*"):
				continue
			if "--" in line:
				line = line.split("--", 1)[0]
			authors.append(line.strip(" *\r\n"))
		f.close()
		authors.sort()
	except Exception, err:
		authors = "[Error: %s]" % err
	return authors

with open('README.md') as file:
	long_description = file.read()

setup(
	name='pyping',
	version='0.0.1',
	description='A pure python ICMP ping implementation using raw sockets.',
#	long_description=long_description,
	author=get_authors(),
	author_email="geoffrey@lehee.name",
	url='https://github.com/socketubs/pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["scripts/pyping"]
)
