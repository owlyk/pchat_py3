import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12451))
server.listen(5)

def handle_client(con, addr):
    def send_data():
        while True:
            try:
                send = input(">>")
                if send.lower() == 'exit':
                    break
                con.send(send.encode())
            except Exception as e:
                print(f"Error sending data: {e}")
                break
        con.close()

    def recv_data():
        while True:
            try:
                data_recv = con.recv(1024)
                if not data_recv:
                    break
                print(data_recv.decode())
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
        con.close()

    threading.Thread(target=send_data).start()
    threading.Thread(target=recv_data).start()

con, addr = server.accept()
handle_client(con, addr)