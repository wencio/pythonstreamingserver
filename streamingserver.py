import socket

# Server parameters
host = "0.0.0.0"  # Listen on all available interfaces
port = 9000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)
print("Listening on {}:{}".format(host, port))

# Continuously listen for incoming connections and handle them
while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(*client_address))

    # Receive data from the client
    data = client_socket.recv(1024)

    # Send the data back to the client
    client_socket.sendall(data)

    # Close the connection
    client_socket.close()
