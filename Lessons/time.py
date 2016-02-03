#!/usr/bin/python

import time

print time.time()	#	returns ticks since epoch

localtime = time.asctime( time.localtime(time.time()) )		# asctime returns formatted time	Tue Jan 13 10:17:09 2009
print localtime


######

import calendar

cal = calendar.month(2016, 2)
print cal

leap = calendar.isleap(2016)

print leap

year = 2000

while year <> 2100:
	if calendar.isleap(year) == True:
		print year
	year += 1
	

