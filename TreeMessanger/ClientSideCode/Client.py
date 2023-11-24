import socket
import threading
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import simpledialog
from ttkbootstrap.constants import *



#--------------------------------BUTTON FUNCTIONS---------------------------------------------------------------#
def update_message_display(message):
    message_display.config(state=tk.NORMAL)
    message_display.insert(tk.END, message + "\n")
    message_display.see(tk.END)
    message_display.config(state=tk.DISABLED)

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
            update_message_display(f"Server: {message}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message():
    message = Messager.get()
    if message:  
        client.send(message.encode('utf-8'))
        update_message_display(f"{message}") 
        Messager.delete(0, tk.END)



#---------------------------------------------------------------------------------------------------------------#


#-------------------------------THIS CODE SENDS THE DATA TO THE SERVER------------------------------------------#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()
#---------------------------------------------------------------------------------------------------------------#

#--------------------------------------------UI-----------------------------------------------------------------#

window = tk.Tk()                                                                                
window.title("Tree Messenger")                                                                  
style = ttk.Style("darkly")                                                                              
window.geometry("500x500")                                                                      
window.resizable(False,False)                                                                   
img = ttk.PhotoImage(file='../Images/Tree.png', width=50)
window.iconphoto(False, img)



message_display = tk.Text(window, height=25, width=78)
message_display.place(x=10, y=25)
message_display.config(state=tk.DISABLED)



label = ttk.Label(window, text="Tree Messsanger", font=('Arial', 12),foreground="green")
label.pack()

Messager = ttk.Entry(window, width=78)
Messager.place(x=10, y=460)

button1 = ttk.Button(text='Send', command=send_message)
button1.place(x=450, y=460)

window.mainloop()
#---------------------------------------------------------------------------------------------------------------#



