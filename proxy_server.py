import socket
host = "www.google.com"
port = 80
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as proxy_start:
	proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	proxy_start.bind((HOST,PORT))
	proxy_start.listen(1)
	while True:
		conn,addr = proxy_start.accept()
		with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:
			remote_ip = socket.gethostbyname(host)
			proxy_end.connect((remote_ip,port))
			send_full_data = conn.recv(BUFFER_SIZE)
			proxy_end.sendall(send_full_data)
			proxy_end.shutdown(socket.SHUT_WR)
			data = proxy_end.recv(BUFFER_SIZE)
			conn.send(data)
		conn.close()