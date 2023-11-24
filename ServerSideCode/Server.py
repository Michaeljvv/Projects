import socket
import threading

# Function to handle incoming messages from clients
def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message from {address}: {message}")
            
            # Send the received message to all connected clients (broadcast)
            for c in clients:
                if c != client_socket:
                    c.send(message.encode('utf-8'))
        except:
            break

# List to store connected clients
clients = []

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP and port
server.bind(('127.0.0.1', 5555))

# Listen for incoming connections
server.listen(5)
print("Server is listening for incoming connections...")

while True:
    # Accept incoming connection
    client_socket, address = server.accept()
    print(f"Connection from {address} has been established!")

    # Add the new client to the list
    clients.append(client_socket)

    # Create a thread to handle the new client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
