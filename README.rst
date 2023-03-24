Python PIDFile
==============

.. image:: https://github.com/mosquito/python-pidfile/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/mosquito/python-pidfile/actions/workflows/tests.yml
   :alt: Github Actions

.. image:: https://img.shields.io/pypi/v/python-pidfile.svg
   :target: https://pypi.python.org/pypi/python-pidfile/
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/python-pidfile.svg
   :target: https://pypi.python.org/pypi/python-pidfile/
   :alt: round wheels

.. image:: https://img.shields.io/pypi/pyversions/python-pidfile.svg
   :target: https://pypi.python.org/pypi/python-pidfile/
   :alt: Python versions

.. image:: https://img.shields.io/pypi/l/python-pidfile.svg
   :target: https://pypi.python.org/pypi/python-pidfile/
   :alt: License

.. image:: https://coveralls.io/repos/github/CostantinoGrana/python-pidfile/badge.svg?branch=master
   :target: https://coveralls.io/github/CostantinoGrana/python-pidfile?branch=master
   :alt: Coverage Status


Python context manager for managing pid files. Example usage:

.. code-block:: python

    import pidfile
    import time

    print('Starting process')
    try:
        with pidfile.PIDFile("/var/run/example.pid"):
            print('Process started')
            time.sleep(30)
    except pidfile.AlreadyRunningError:
        print('Already running.')

    print('Exiting')

The context manager will take care of verifying the existence of a pid file,
check its pid to see if it's alive, check the command line (which should be `<something>/<python name>`), and
if all the conditions are met, rise a `pidfile.AlreadyRunningError` exception.

`PIDFile()` defaults to `pidfile` for the file name, but it's possible to specify another, e.g. `PIDFile('foobar.pid')`.


Under the hood
--------------

The algorithm of the library is very simple, at startup, a file is created,
and after checking that another instance of the program is not running, the
current process ID is written to it.

The check works as follows:

* If the file does not exist, then the check is passed.
* An identifier is written in the file, it is read and checked that a
  process running with such an identifier exists, and has the same command line.
