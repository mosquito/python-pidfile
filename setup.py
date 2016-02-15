#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages

import os
import pidfile


setup(
    name='python-pidfile',
    version=pidfile.__version__,
    author=pidfile.__author__,
    author_email=", ".join(map(lambda x: x[1], pidfile.author_info)),
    url="https://github.com/mosquito/python-pidfile",
    license="MIT",
    description="PIDFile context processor. Supported py2 and py3",
    long_description=open('README.rst').read(),
    platforms="unix",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    zip_safe=True,
    packages=find_packages(exclude=('tests',)),
)
