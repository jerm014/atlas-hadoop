#!/usr/bin/python2.7
"""Python 2.7 is required for SnakeBite from Spotify"""
from snakebite.client import Client


def createdir(l):
    """documentation"""
    client = Client("localhost", 9000)

    for dir in l:
        for result in client.mkdir([dir], create_parent=True):
            print(result)
