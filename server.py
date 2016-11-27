import socket
import time
import threading

def toplink(sock, addr):
	print 'Accept new connection from %s:%s...' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s!' % data)
	sock.close()
	print 'Connection from %s:%s closed.' % addr

host = socket.gethostname()
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()
