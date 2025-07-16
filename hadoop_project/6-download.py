#!/usr/bin/python2.7
"""Python 2.7 required for snakebite"""
from snakebite.client import Client


def download(l):
    """documentation goes here!"""
    client = Client('hadoop3', 9000)
    for file_path in l:
        target = '/tmp/' + os.path.basename(file_path)

        if os.path.exists(target):
            print({'path': target_path, 'result': False, 'error': 'file exists', 'source_path': file_path})
            continue

        try:
            for f in client.copyToLocal([file_path], '/tmp'):
                res = f.get('result', True)
                error = f.get('error', '')
                print({'path': target, 'result': res, 'error': error, 'source_path': file_path})

        except Exception as e:
            print({'path': target, 'result': False, 'error': str(e), 'source_path': file_path})
