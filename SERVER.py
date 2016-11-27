import socket

host = socket.gethostname()
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print "Linked"
info = sock.recv(1024)
while info != "exit":
	print "From Ohters : " + info
	send_mes = raw_input("")
	sock.send(send_mes)
	if send_mes == "exit":
		break
	info = sock.recv(1024)
sock.close()
s.close()
