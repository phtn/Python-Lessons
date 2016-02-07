#!/usr/bin/env python3

import cgi

print('Content-type:text/html\r\n\r\n')

print("<html><body>")

print("<h3> Hello Apache! </h3>")

for i in range(5):
	print ("<h4> !!! " + str(i) + "</h4>")

form = cgi.FieldStorage()

if form.getvalue("name"):
	name = form.getvalue("name")
	print("<h4>" + name + "</h4")

if form.getvalue("happy"):
	print("<p> Yay! </p>")

if form.getvalue("sad"):
	print("<p> Oh no! </p>")

print("<form method='post' action='apache.py'>")
print("<p> Name: <input type='text' name='name'/>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")

print("</body></html>")