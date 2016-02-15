Python PIDFile
==============

.. image:: https://travis-ci.org/mosquito/python-pidfile.svg?branch=master
    :target: https://travis-ci.org/mosquito/python-pidfile

.. image:: https://img.shields.io/pypi/v/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/

.. image:: https://img.shields.io/pypi/pyversions/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/

.. image:: https://img.shields.io/pypi/l/python-pidfile.svg
    :target: https://pypi.python.org/pypi/python-pidfile/


Python context processor for ensure once execution of program::

    from pidfile import pidfile

    if __name__ == "__main__":
        
        with PIDFile("/var/run/myprogram.pid"):
            pass


