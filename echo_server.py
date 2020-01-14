import socket, time

HOST = "" # Symbolic name meaning all available interfaces
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #Set the value of the given socket option 
        s.bind((HOST,PORT)) 
        s.listen(2) #Listen for connections made to the socket.
        while True:
            conn,addr = s.accept() #Accept a connection. 
            # where conn is a new socket object usable to 
            # send and receive data on the connection, 
            # and address is the address bound to the socket on the other end of the connection.
            print("Connected by", conn, addr)
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data) #Send data to the socket. The socket must be connected to a remote socket
            conn.close()

if __name__ == "__main__":
    main()