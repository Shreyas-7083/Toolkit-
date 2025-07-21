import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 55555

class ChatClientApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_history.pack(fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(fill=tk.X, padx=10, pady=5)
        self.message_entry.bind("<Return>", self.send_message)

        self.connect_to_server()

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_history.insert(tk.END, message + '\n')
                self.chat_history.see(tk.END)  # Scroll to the bottom
            except:
                break

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ChatClientApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
