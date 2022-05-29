import json
from typing import re

import requests

# response = requests.get('https://httpbin.org/get')
# print(response.text)
# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# response = requests.post('https://httpbin.org/post', data=json.dumps({'key': 'value'}))
# response = requests.post('https://httpbin.org/post', json={'key': 'value'})
# print(response.text)
# ======================================
# url = 'https://httpbin.org/post'
# files = {
#     'file':
#         {'./test.txt',
#          open('test.txt', 'rb')}
# }
# r = requests.post(url, files=files)
# print(r.text)
# ======================================
# url = 'https://httpbin.org/get'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r.text)

#
# url = "https://playground.learnqa.ru/api/get_301"
# r = requests.post(url, allow_redirects=True)
# first_r = r.history[0]
# second_r = r
# print(first_r.url)
# print(second_r.url)

url = "https://playground.learnqa.ru/api/get_auth_cookie"
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post(url, data=payload)
# print(response1.text)
# print(response1.status_code)
# print(dict(response1.cookies))
cookie_value = response1.cookies.get('auth_cookie')

cookies = {'auth_cookie': cookie_value}
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})
url2 = "https://playground.learnqa.ru/api/check_auth_cookie"
response2 = requests.post(url2, cookies=cookies)

print(response2.text)
