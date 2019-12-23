author_info = (
    ("Dmitry Orlov", "me@mosquito.su"),
    ("Costantino Grana", ""),
    ("Lorenzo Baraldi", ""),
    ("Michele Cancilla", ""),
)

version_info = (3, 0, 0)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{0} <{1}>".format(*author) for author in author_info)
