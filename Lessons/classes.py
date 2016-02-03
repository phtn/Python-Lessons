#!/usr/bin/python

class Employee:
	'Employees Class'					#	Optional Documentation String
	count = 0							#	Class Variable

	def __init__( self, name, age ):
		self.name = name
		self.age = age
		Employee.count += 1

	def empCount(self):
		print Employee.count

	def empInfo(self):
		print self.name, self.age


emp1 = Employee('Sarah', 42)			#	Add Objects
emp2 = Employee('Jessica', 25)

emp1.empCount()
emp1.empInfo()

emp1.age = 23							#	Modify Attributes
emp1.phone = '7072056478'				# 	Add Attributes
del emp1.phone							#	Remove Attributes


hasattr(emp1, 'age')    				# 	Returns true if 'age' attribute exists
getattr(emp1, 'age')    				# 	Returns value of 'age' attribute
#setattr(emp1, 'age', 8) 				# 	Set attribute 'age' at 8
#delattr(empl, 'age')    				# 	Delete attribute 'age'

print 'doc:',Employee.__doc__
print 'name:', Employee.__name__
print 'module:', Employee.__module__
print 'bases:', Employee.__bases__
print 'dict:', Employee.__dict__