import socket
import threading

host = '127.0.0.1'
port = 12345


class ServerNode:
    def __init__(self):
        try:
            self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port_and_ip = (host, port)
            self.node.bind(port_and_ip)
            self.node.listen(5)
            self.connection, addr = self.node.accept()
            print(addr[0] + ' connected')
        except socket.error as e:
            print('error')

    def send_sms(self, SMS):
        print('send_sms')
        self.connection.send(SMS.encode())

    def receive_sms(self):
        print('receive_sms')
        while True:
            data = self.connection.recv(1024).decode()
            print(data)

    def main(self):
        print('main')
        while True:
            message = input()
            self.send_sms(message)


server = ServerNode()
always_receive = threading.Thread(target=server.receive_sms)
always_receive.daemon = True
always_receive.start()
server.main()
