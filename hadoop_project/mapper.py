#!/usr/bin/python2.7
"""Use Python 2.7 for this project"""
import sys
import csv

reader = csv.reader(sys.stdin)

try:
    next(reader)
except StopIteration:
    sys.exit()

for row in reader:
    try:
        record_id = row[0].strip()
        company = row[1].strip()
        compensation = row[4].strip()

        int(compensation) 

        print(f"{record_id}\t{company},{compensation}")

    except (IndexError, ValueError):
        continue
