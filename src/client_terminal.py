import threading
import socket

client = socket.socket()
client.connect(('localhost', 12451))

def recv():
    while True:
        data_get = client.recv(1024)
        print(data_get.decode())

def send():
    while True:
        text = input(">>")
        client.send(text.encode())

threading.Thread(target=send).start()
threading.Thread(target=recv).start()