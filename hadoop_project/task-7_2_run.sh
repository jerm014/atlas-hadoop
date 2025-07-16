#!/bin/bash

# The -output flag directs all results to /holbies/output/
mapred streaming \
  -files mapper.py,reducer.py \
  -input /holbies/input/salaries.csv \
  -output /holbies/output \
  -mapper ./mapper.py \
  -reducer ./reducer.py
