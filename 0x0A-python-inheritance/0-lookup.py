#!/usr/bin/python3
"""Defines an obj attribute lookup func."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
