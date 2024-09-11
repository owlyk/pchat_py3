import threading
import socket
from tkinter import *

server = socket.socket()
server.bind(('localhost', 63453))
server.listen(2)
con, addr = server.accept()

root = Tk()

def send():
    data_send = edit_Text.get()
    if data_send:
        con.send(data_send.encode())
        label = Label(root, text=data_send, bg="red", fg="white")
        label.pack(side=TOP, fill=X)
        edit_Text.delete(0, END)

def recv():
    while True:
        data_recv = con.recv(1024).decode()
        if not data_recv:
            break
        label = Label(root, text=data_recv, bg="blue", fg="white")
        label.pack(side=TOP, fill=X)

button = Button(root, text="Send", command=send)
edit_Text = Entry(root)

button.pack(fill=X, side=BOTTOM)
edit_Text.pack(fill=X, side=BOTTOM)

threading.Thread(target=recv).start()

root.geometry("400x600")
root.title("server")
root.resizable(width=False, height=False)

root.mainloop()