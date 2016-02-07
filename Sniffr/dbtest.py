#!/usr/bin/env python3

import sqlite3

def main():

	try:
		conn = sqlite3.connect('test.db')

		curs = conn.cursor()

		curs.execute('CREATE TABLE Colors(Id INT, Name TEXT, Hex TEXT)')
		curs.execute('INSERT INTO Colors VALUES(1, "Red", "Blood")')
		curs.execute('INSERT INTO Colors VALUES(2, "Green", "Grass")')
		curs.execute('INSERT INTO Colors VALUES(3, "Blue", "Sky")')

		conn.commit()

		curs.execute('SELECT * FROM Colors')
		
		data = curs.fetchall()

		for row in data:
			print(row)

		#curs.execute('SELECT SQLITE_VERSION()')

		#data = curs.fetchone()

		#print(data)

	except sqlite3.Error:
		if conn:
			print("Error!")
			conn.rollback()

	finally:
		if conn:
			conn.close()


if __name__ == '__main__':
	main()