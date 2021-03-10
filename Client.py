import socket
import threading

host = '127.0.0.1'
port = 12345


class ClientNode:
    def __init__(self):
        try:
            self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port_and_ip = (host, port)
            self.node.connect(port_and_ip)
        except socket.error as e:
            print('not connect server')

    def send_sms(self, SMS):
        self.node.send(SMS.encode())

    def receive_sms(self):
        while True:
            data = self.node.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            message = input()
            self.send_sms(message)


Client = ClientNode()
always_receive = threading.Thread(target=Client.receive_sms)
always_receive.daemon = True
always_receive.start()
Client.main()
