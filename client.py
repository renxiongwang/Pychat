import socket

host = socket.gethostname()
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()
