#!/usr/bin/env python

import sys

data=[]

for line_in in sys.stdin:
    line = line_in.strip()
    if line not in data:
        data.append(line)
        print(line)
