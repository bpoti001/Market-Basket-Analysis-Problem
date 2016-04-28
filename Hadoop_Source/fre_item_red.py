#!/usr/bin/env python
import sys
last_key = None
for this_key in sys.stdin:
    if this_key!=last_key:
    	print this_key
    last_key = this_key
