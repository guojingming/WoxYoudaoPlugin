import sys
import math
import time

import hashlib
import requests

def getMd5(src):
    m = hashlib.md5(src.encode())
    return m.hexdigest().lower()

def processContent(oriContent):
    resArray = []
    index = oriContent.find(b'{"value":[')
    while index != -1:
        oriContent = oriContent[index + len('{"value":['):]
        tempStr = '],"key":"'
        index = oriContent.find(bytes(tempStr, encoding="utf8"))
        if index == -1:
            break
        resArray.append(oriContent[:index])
        index = oriContent.find(b'{"value":[')
    return resArray

def getTranslationResult(queryWord):
    apiUrl = "http://openapi.youdao.com/api"
    appId = "3307d4aaa19ac4b2"
    appKey = "6QvF1i4mkZOEGlE5HnZA8CJEg1VzOnCS"
    salt = "2"
    originalText = appId + queryWord + salt + appKey
    sign = getMd5(originalText)
    params = "?q=" + queryWord + "&from=EN&to=zh_CHS&appKey=" + appId + "&salt=" + salt + "&sign=" + sign
    url = apiUrl + params
    r = requests.get(url)
    #message = {"url": url, "errorCode": r.status_code, "content": r.content}
    resArray = []
    if r.status_code == 200:
        resArray = processContent(r.content)
    return resArray
#test_http()