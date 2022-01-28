#!/usr/bin/python3


"""this module will be used for voting 4096 times
    at the website provided"""
import urllib
from bs4 import BeautifulSoup
import requests

failed = 0

url = "http://158.69.76.135/level1.php"
for i in range(0, 4096):
    session = requests.session()
    get_key_r = session.get(url)
    content = get_key_r.content
    soup = BeautifulSoup(content, 'html.parser')
    inputs = soup.find_all('input')
    for line in inputs:
        if line.get('name') == "key":
            key = line.get('value')
    
    payload = {'id': '496', 'key': key, 'holdthedoor': 'submit'}
    r = session.post(url, data=payload)
    if r.status_code != 200:
        print("failed to post {}th request".format(i))
        failed += 1
    if i % 10 == 0:
        print("posted 10 requests to server")
    del session
print("Failed {} number of requests".format(failed))
