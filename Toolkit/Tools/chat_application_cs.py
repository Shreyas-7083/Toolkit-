import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# List to store client connections
clients = []

# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If no message received, disconnect client
                remove_client(client_socket)
                break
            # Broadcast message to all clients
            broadcast(message)
        except:
            # If an error occurs, disconnect client
            remove_client(client_socket)
            break

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

# Function to remove client from list
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

# Function to accept client connections
def accept_connections():
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")
        # Create a thread to handle each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Start the server
def start_server():
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    accept_connections()

if __name__ == "__main__":
    start_server()
