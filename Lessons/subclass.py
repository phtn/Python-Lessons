#!/usr/bin/python

class Parent:
	'Parent Class'
	count = 0

	def __init__(self, name):
		self.name = name
		print "Parent Constructor init"

	def parentMethod(self):
		print "Calling Parent Class Method"

	def setAttr(self, attr):
		Parent.count = attr

	def getAttr(self):
		print Parent.count

class Child(Parent):

	def __init__(self):
		print "Child Constructor init"

	def childMethod(self):
		print "Calling Child Class Method"


c = Child()
#p = Parent()
print c.childMethod()
person1 = Parent('Zara')
print c.count
print Parent.count
