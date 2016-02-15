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
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=True,
    packages=find_packages(exclude=('tests',)),
)
