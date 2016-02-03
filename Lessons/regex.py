#!/usr/bin/python

import re

lineText = 'Pale blue dot'

findMatch = re.match('(.*) blue (.*?)', lineText, re.M | re.I)

if findMatch:
	#print findMatch.group(0)
	print findMatch.group(1)
	#print findMatch.group(2)
else:
	print 'Nothing else matters.'


searcher = re.search('(.*) blue (.*?)', lineText, re.M | re.I)

if searcher:
	#print searcher.group(0)
	print searcher.group(1)


mynote = '707-205-6478 is my phone number';

phone = re.sub(r'is.*$','',mynote)

number = re.sub(r'\D','', mynote)

print phone
print number