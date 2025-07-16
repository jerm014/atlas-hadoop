#!/usr/bin/python2.7
"""Use Python 2.7 for this project"""
import sys


for input in sys.stdin:
    input = input.strip()
    fields = input.split(",")

    if len(fields) >= 3:
        id = fields[0]
        company = fields[1]
        total_yearly_compensation = fields[3]
        print "{}\t{},{}".format(id, company, total_yearly_compensation)
