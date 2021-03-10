import threading
import socket

host = '127.0.0.1'
port = 59008
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


def broadcast(message):
    for client in clients:
        client.send(message)


def main():
    while True:
        enter = input()
        if enter == 'attack':
            print('2323232323')
            broadcast('attack'.encode('utf-8'))
        else:
            message = "server: " + enter
            print('test' + message)
            broadcast(str(message).encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

send_thread = threading.Thread(target=main)
send_thread.start()