Python PIDFile
==============

.. image:: https://travis-ci.org/CostantinoGrana/python-pidfile.svg?branch=master
    :target: https://travis-ci.org/CostantinoGrana/python-pidfile

.. image:: https://img.shields.io/pypi/v/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/

.. image:: https://img.shields.io/pypi/pyversions/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/

.. image:: https://img.shields.io/pypi/l/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/

.. image:: https://coveralls.io/repos/github/CostantinoGrana/python-pidfile/badge.svg?branch=master
    :target: https://coveralls.io/github/CostantinoGrana/python-pidfile?branch=master



Python context manager for manage pid files:

.. code-block:: python

    from pidfile import PIDFile

    if __name__ == "__main__":
        
        with PIDFile("/var/run/myprogram.pid"):
            print('Hello world')
