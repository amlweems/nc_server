#!/usr/bin/env python
import socket

def send(data):
	print data
	return data.encode('rot13')

HOST = '0.0.0.0'
PORT = 7776
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
try:
	print "Running server on port", PORT
	print "Press ^C to close the socket"
	while True:
		conn, addr = s.accept()
		print 'Connected by', ':'.join([str(i) for i in addr])
		try:
			while True:
			    data = conn.recv(1024)
			    if not data: break
			    conn.send(send(data))
		except Exception as e:
			print e
		finally:
			conn.close()
except:
	pass
finally:
		s.close()
