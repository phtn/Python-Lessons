#!/usr/bin/python

a = 6
b = 8
c = 0

print (a**b)    # exponent
print (b//a)    # quotient
print (a<>b)    # not equal to
print (a==b)    # equal to

# IF Statements with WHILE

if (a == 6):
    print 'six'
    while c <> 10:
        print c
        c+=5
else:
    while c <> 10:
        print c
        c+=1

# FOR loop

for letter in 'phtn':
    print letter

colours = ['red', 'blue', 'green']

for index in range(len(colours)):
    print colours[index]

for colour in colours:
    if (colour == 'blue'):
        pass
        print 'just passing through'
    print colour

# Numbers

import math

print math.ceil(4.55)
print math.floor(4.55)
print math.pi
print math.e
print math.sqrt(9)
print pow(3,2)

print '1.5 radian to degrees: ',math.degrees(1.5)

# Random

import random

print random.randrange(0, 100, 5)

# Strings
s1 = 'hellO'

print s1
print 'go to', s1[0:4]
print 'h' in s1
print str.capitalize(s1)
print str.isupper(s1[0])
print str.title(s1)
print str.upper(s1)
print max(s1)
print min(s1)

s2 = u'222'
print s2.isdecimal()    # returns true if string are decimal


# Lists

l1 = ['red', 'blue', 'green', 'yellow']

print l1
print l1[0:2]

l1[3] = 'alpha'

print l1

for i in l1:
    print i

l1.append('black')

print max(l1)
print min(l1)
print len(l1)
print l1.count('red')

l1.sort()
print l1


