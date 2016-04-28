#!/usr/bin/env python
import sys
datasets1 = []
for line1 in sys.stdin:
    line1 = line1.strip( )
    items1 = line1.split(' ')
    datasets1.append(items1)
datasets1= map(set,datasets1)


datasets2 = []
#reduce1_output=open('reduce1out','r')
for line2 in open('part-00000','r'):
    line2 = line2.strip( )
    if line2:
        items2 = line2.split(' ')  
        datasets2.append(items2)
datasets2= map(frozenset,datasets2)

for i in datasets1:
    for j in datasets2:
        if j.issubset(i):
            print "%s\t%d" % (j,1)
