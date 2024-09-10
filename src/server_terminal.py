import threading
import socket

server = socket.socket()
server.bind(('localhost', 12451))
server.listen(5)

def handle_client(con, addr):
    def send_data():
        while True:
            try:
                send = input(">>")
                con.send(send.encode())
            except (BrokenPipeError, ConnectionResetError):
                break

    def recv_data():
        while True:
            try:
                data_recv = con.recv(1024)
                if not data_recv:
                    break
                print(data_recv.decode())
            except ConnectionResetError:
                break

    threading.Thread(target=send_data).start()
    threading.Thread(target=recv_data).start()

while True:
    try:
        con, addr = server.accept()
        handle_client(con, addr)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")

server.close()