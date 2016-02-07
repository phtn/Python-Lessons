#!/usr/bin/env python3

import socket
import struct
import textwrap

# the public network interface


#print HOST

def main():
	#HOST = socket.gethostbyname(socket.gethostname())
	#print('IP: {}'.format(HOST))
	
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	#raw_data, addr = conn.recvfrom(65536)
	#print(conn)
	#print(raw_data)

	#dest_mac, src_mac, protocol = struct.unpack('! 6s 6s H', raw_data[:14])
	#conn.bind((HOST, 0))
	#conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	#conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	
	#print(get_mac_addr(dest_mac), raw_data[14:])

	while True:
		raw_data, addr = conn.recvfrom(65536)
		dest_mac, src_mac, ether_proto, data = e_frame(raw_data)
		print ('\n Ethernet Frame')
		print ('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, ether_proto))


# unpacking ethernet frame (eframe)
def e_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]


# format MAC address
def get_mac_addr(bytes_addr):
	bytes_str = map('{:02x}'.format, bytes_addr)
	return ':'.join(bytes_addr).upper()


main()