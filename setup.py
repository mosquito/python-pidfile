import sys
import os
from setuptools import setup, find_packages


version_file = os.path.join('pidfile', 'version.py')

if sys.version_info < (3,):
    import imp
    version = imp.load_source('version', version_file)
elif sys.version_info < (3, 5):
    from importlib.machinery import SourceFileLoader
    version = SourceFileLoader("version", version_file).load_module()
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("version", version_file)
    version = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(version)


setup(
    name='python-pidfile',
    version=version.__version__,
    author=version.__author__,
    author_email=", ".join(
        filter(None, map(lambda x: x[1], version.author_info))
    ),
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'psutil'
    ],
    extras_require={
        'develop': [
            'coverage!=4.3',
            'coveralls',
            'pylama',
            'pytest',
            'pytest-cov',
            'mock',
        ],
    }
)
