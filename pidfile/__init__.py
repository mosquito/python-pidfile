import os

author_info = (
    ("Dmitry Orlov", "me@mosquito.su"),
)

version_info = (1, 0, 2)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{0} <{1}>".format(*author) for author in author_info)

from .pidfile import PIDFile

__all__ = ('PIDFile',)
