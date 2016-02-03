#!/usr/bin/python
'''
file1 = open('testfile.txt', 'r')	#	(r)	Read - only

#print file1.name

file1.close()


file2 = open('testfile.txt', 'wb')	#	(wb)	Write Binary

#file2.write('cosmos')

#print file2.name

file2.close()

'''
file3 = open('testfile.txt', 'r+')	#	(r+)	Read & Write

file3.write('cosmos')

title = file3.read(2)
reposition = file3.seek(1,0)
position = file3.tell();

print title
print position

file3.close()

import os

print os.getcwd()