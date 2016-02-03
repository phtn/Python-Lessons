#!/usr/bin/python

dict = {'name': 'Becka', 'age': 24}



dict['age'] = 23		#	update value

dict['state'] = 'PA'	#	add new entry

print dict['name']
print dict['age']
print dict['state']

del dict['state']		#	delete entry

dict.clear()			#	delete all entries in dict

del dict			#	delete entire dictionary	