author_info = (
    ("Dmitry Orlov", "me@mosquito.su"),
)

version_info = (2, 0, 0)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{0} <{1}>".format(*author) for author in author_info)
