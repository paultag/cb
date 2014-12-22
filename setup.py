#!/usr/bin/env python

from setuptools import setup

long_description = open('README.md', 'r').read()

setup(
    name="cb",
    version="0.1",
    packages=['cb',],
    package_data={'cb': ['*.hy'],},
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='does some stuff with things & stuff',
    entry_points={
        'console_scripts': [
            'cb = cb.cli:cb',
        ]
    },
    license="Expat",
    url="",
    platforms=['any']
)
