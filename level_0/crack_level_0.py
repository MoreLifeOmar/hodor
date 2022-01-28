#!/usr/bin/python3


"""this module will be used for voting 1024 times
    at the website provided"""
import requests
import time

payload = {'id': '496', 'holdthedoor': 'Submit'}
failed = 0

for i in range(0, 1024):
    r = requests.post("http://158.69.76.135/level0.php", data=payload)
    if r.status_code != 200:
        print("failed to post {}th request".format(i))
        failed += 1

print("Failed {} number of requests".format(failed))
