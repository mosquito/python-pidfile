Python PIDFile
==============

[![Build Status](https://travis-ci.org/CostantinoGrana/python-pidfile.svg?branch=master)](https://travis-ci.org/CostantinoGrana/python-pidfile)
[![Latest Version](https://img.shields.io/pypi/v/python-pidfile.svg)](https://pypi.python.org/pypi/python-pidfile/)
[![](https://img.shields.io/pypi/wheel/python-pidfile.svg)](https://pypi.python.org/pypi/python-pidfile/)
[![](https://img.shields.io/pypi/pyversions/python-pidfile.svg)](https://pypi.python.org/pypi/python-pidfile/)
[![](https://img.shields.io/pypi/l/python-pidfile.svg)](https://pypi.python.org/pypi/python-pidfile/)
[![Coverage Status](https://coveralls.io/repos/github/CostantinoGrana/python-pidfile/badge.svg?branch=master)](https://coveralls.io/github/CostantinoGrana/python-pidfile?branch=master)

Python context manager for managing pid files. Example usage:

```python
import pidfile
import time

print('1')
try:
    with pidfile.PIDFile():
        print('2')
        time.sleep(30)
except pidfile.AlreadyRunningError:
    print('Already running.')
print('3')
```

The context manager will take care of verifying the existence of a pid file,
check its pid to see if it's alive, check the command line (which should be `<something>/<python name>`), and
if all the conditions are met, rise a `pidfile.AlreadyRunningError` exception.

`PIDFile()` defaults to `pidfile` for the file name, but it's possible to specify another, e.g. `PIDFile('foobar.pid')`.
