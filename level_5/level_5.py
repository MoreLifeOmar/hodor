#!/usr/bin/python3

import requests
import cv2
import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# level 5


def send_votes(id, times):
    url = 'http://158.69.76.135/level5.php'
    captcha_url = 'http://158.69.76.135/tim.php'
    string_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

    for i in range(times):

        with requests.Session() as s:
            r = s.get(url, headers={'User-Agent': string_agent})
            i = s.get(captcha_url, headers={'User-Agent': string_agent, 'referer': url})
            with open('tim.png', 'wb') as image_file:
                image_file.write(i.content)
            captcha_string = translate_image('tim.png')
            print(captcha_string)
            c = r.cookies
            key_form = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key_form = cookie.value
                    break

            s.post(url, data={'id': id, 'holdthedoor': 'Enviar', 'key': key_form, 'captcha': captcha_string},
                   headers={'User-Agent': string_agent, 'referer': url},
                   cookies=c)


def clean_image(file):
    img = cv2.imread(file, 0)

    kernel = np.ones((2, 2), np.uint8)

    img_dilation = cv2.dilate(img, kernel, iterations=1)
    img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

    cv2.imwrite('input.png', img)
    cv2.imwrite('erosion.png', img_erosion)
    cv2.imwrite('dilation.png', img_dilation)


def translate_image(file):
    clean_image(file)
    captcha_string = pytesseract.image_to_string(Image.open('dilation.png'))
    return captcha_string


send_votes(867, 1)
