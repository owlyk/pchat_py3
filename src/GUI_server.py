import threading
import socket
from tkinter import *

server = socket.socket()
server.bind(('localhost', 63453))
server.listen(2)

try:
    con, addr = server.accept()
except Exception as e:
    print(f"Error accepting connection: {e}")
    server.close()
    exit()

root = Tk()

def send():
    if con:
        data_send = edit_Text.get().encode('utf-8')
        con.send(data_send)
        label = Label(root, text=data_send.decode('utf-8'), bg="red", fg="white")
        label.pack(side=TOP, fill=X)
        edit_Text.delete(0, END)

def recv():
    while True:
        try:
            data_recv = con.recv(1024)
            if not data_recv:
                break
            label = Label(root, text=data_recv.decode('utf-8'), bg="blue", fg="white")
            label.pack(side=TOP, fill=X)
        except Exception as e:
            break

button = Button(root, text="Send", command=send)
edit_Text = Entry(root)

button.pack(fill=X, side=BOTTOM)
edit_Text.pack(fill=X, side=BOTTOM)

threading.Thread(target=recv, daemon=True).start()

root.geometry("400x600")
root.title("server")
root.resizable(width=False, height=False)

def on_closing():
    if 'con' in locals():
        con.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()