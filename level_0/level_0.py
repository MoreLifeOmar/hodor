#!/usr/bin/python3
import requests
import sys

#level 0

url = 'http://158.69.76.135/level0.php'
cookie_list = []
id = 10320
times = 1024

for i in range(times):
    response_get = requests.post(url, data={'id': id, 'holdthedoor': 'Enviar'})
