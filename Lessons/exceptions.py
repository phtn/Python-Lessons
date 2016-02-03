#!/usr/bin/python

try:
	file1 = open('testfile2.txt', 'r')
	print file1.name
	file1.close()

except IOError, Argument:
	print 'File 1:',Argument

else:
	print 'file is open'


try: 
	file2 = open('testfile.txt', 'r')
	print 'File 2:',file2.name
	file2.close()
finally:
	print 'Successful!'

