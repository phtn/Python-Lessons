#!/usr/bin/env python3

import socket

def main():
	host = '127.0.0.1'
	port = 3000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("SERVER STARTED")

	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print("message from: " + str(addr))
		print("from user: " + data )
		data = data.upper()
		print(data)
		s.sendto(data.encode('utf-8'), addr)
	s.close()

if __name__ == '__main__':
	main()