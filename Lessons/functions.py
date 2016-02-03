#!/usr/bin/python

#	Basic Functions

def func1 ( str ):
	print str
	#return str

#func1('print this string.')

def func2 ( name, age ):
	print 'Name:', name
	print 'Age:', age
	#return

#func2 ( 'Becka', 23 )

#func2( age='24', name='Rebecka')

def func3 ( num ):
	while num <> 6:
		print num
		num += 1
	#return

#func3 ( 1 )

#	Lambdas

sum = lambda a, b: a + b

#print sum ( 5, 10 )
