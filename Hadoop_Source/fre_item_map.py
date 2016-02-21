#!/usr/bin/env python
import sys
def createC1(dataset):
	"Create a list of candidate item sets of size one."
	c1 = []
	for transaction in dataset:
		for item in transaction:
			if not [item] in c1:
				c1.append([item])
	c1.sort()
	#frozenset because it will be a ket of a dictionary.
	return map(frozenset, c1)
 
 
def scanD(dataset, candidates, min_support):
	"Returns all candidates that meets a minimum support level"
	sscnt = {}
	for tid in dataset:
		for can in candidates:
			if can.issubset(tid):
				sscnt.setdefault(can, 0)
				sscnt[can] += 1
 
	num_items = float(len(dataset))
	retlist = []
	support_data = {}
	for key in sscnt:
		support = sscnt[key] / num_items
		if support >= min_support:
			retlist.insert(0, key)
		support_data[key] = support
	return retlist, support_data
 
 
def aprioriGen(freq_sets, k):
	"Generate the joint transactions from candidate sets"
	retList = []
	lenLk = len(freq_sets)
	for i in range(lenLk):
		for j in range(i + 1, lenLk):
			L1 = list(freq_sets[i])[:k - 2]
			L2 = list(freq_sets[j])[:k - 2]
			L1.sort()
			L2.sort()
			if L1 == L2:
				retList.append(freq_sets[i] | freq_sets[j])
	return retList
a=[]
#data = open("/root/market.txt")
for i in sys.stdin:
	i = i.strip()
	items = i.split()
	a.append(items)
c1 = createC1(a)
d = map(set,a)
K=2
ps = 0.3
for i in range(K):
	L1,sp = scanD(d,c1,ps)
	c1 = aprioriGen(L1,i+1)
out=[]
for i in L1:
	x,y = i
	x = int(x)
	y = int(y)
	print "%d %d" %(x,y)
#	print z
#	out.append(z)
#for i in out:
#		print i


