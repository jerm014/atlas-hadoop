#!/usr/bin/env python3
"""documentation"""
import sys
import heapq

top_ten = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        parts = line.split('\t')
        if len(parts) != 2:
            continue
            
        record_id = parts[0]
        company_compensation = parts[1].split(',')
        
        if len(company_compensation) != 2:
            continue

        company = company_compensation[0]
        compensation = int(company_compensation[1])
        data = (compensation, record_id, company)

        if len(top_ten) < 10:
            heapq.heappush(top_ten, data)
        else:
            if compensation > top_ten[0][0]:
                heapq.heapreplace(top_ten, data)

    except (ValueError, IndexError):
        continue

top_ten.sort(key=lambda x: x[0], reverse=True)

for compensation, record_id, company in top_ten:
    print(f"{record_id}\t{company},{compensation}")
