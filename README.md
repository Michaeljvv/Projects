# FOR Tree Messenger
This repository contains a simple messenger application built with Python that facilitates communication between clients through a server.

- Overview
Client-side
The client-side code (client.py) is responsible for initiating a connection with the server and providing a graphical user interface (GUI) for users to send and receive messages. It utilizes the socket library for networking and tkinter for the GUI.

- Code Breakdown
update_message_display: Updates the message display area in the GUI.
receive_messages: Runs continuously in a separate thread to receive messages from the server.
send_message: Sends messages entered by the user to the server.
Server-side
The server-side code (server.py) handles incoming connections from clients, relays messages among connected clients, and manages the communication flow.

- Code Breakdown
handle_client: Manages incoming messages from a client and broadcasts them to all connected clients.
clients: Maintains a list of connected clients.
Socket creation, binding, and listening: Establishes a server socket, binds it to a specific IP and port, and listens for incoming connections.
Getting Started
To run this application:

Run server.py to start the server.
Run client.py to initiate the client application.
Interact with the GUI on the client side to send and receive messages.

- Dependencies
ttkbootstrap
tkinter
- Usage
Launch the server before running any clients.
Multiple clients can connect to the server simultaneously and exchange messages.
 mportant Notes
This application currently runs on the localhost (127.0.0.1) and port 5555. Modify these values if needed.
Error handling and edge cases might need further refinement for robustness.

- Contributing
Feel free to contribute by opening issues or submitting pull requests for enhancements, bug fixes, or additional features.

- License
Tis project is licensed under the MIT License.
