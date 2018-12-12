import sys
import math
import time


import hashlib


import requests

def test_http():
    url = "http://openapi.youdao.com/api"
    params = "?q=good&from=EN&to=zh_CHS&appKey=ff889495-4b45-46d9-8f48-946554334f2a&salt=2&sign=1995882C5064805BC30A39829B779D7B"
    r = requests.get(url + params)
    print(r.status_code)
    print(r.content)

def getMd5(src):
    m = hashlib.md5(src.encode())
    return m.hexdigest().upper()


print(getMd5('hello'))
#test_http()