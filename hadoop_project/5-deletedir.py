#!/usr/bin/python2.7
"""Python 2.7 required for snakebite"""
from snakebite.client import Client


def deletedir(l):
    """documentation"""
    client = Client("localhost", 9000)

    for directory in reversed(l):
        for result in client.delete([directory], recurse=True):
            print(result)
