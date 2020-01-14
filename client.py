import socket, sys

host = "www.google.com"
port = 80
payload = 'GET / HTTP/1.0\r\nHost: '+ host + '\r\n\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 4096

remote_ip = socket.gethostbyname(host) # Translate a host name to IPv4 address format.
s.connect((remote_ip,port)) # Connect to a remote socket at address.
s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR) #Shut down one or both halves of the connection.
# further sends are disallowed
full_data = b""
while True:
	data = s.recv(buffer_size)
	if not data:
		break
	full_data += data # server will send an empty message, and the loop will break 
print(full_data)
