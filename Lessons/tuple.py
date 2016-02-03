#!/usr/bin/python

# Tuples | sequence of immutable objects (cannot be changed)

tup1 = (1,2,3)

tup2 = ('a','b','c')
tup3 = (4,5,6,7)

print tup1[0:]

for i in tup1:
    print i

print cmp(tup1,tup3)

print len(tup3)
