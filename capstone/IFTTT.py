import sys
import os
import shutil
import time
import http.client, urllib.parse
import requests as req


evt = 'capstone_test'   # 事件名稱
key = 'mjTQR0ZnbgiHd2hYBJQSu15o3OpfgsajP8_tsVQMEWw' # 你的key
val1 = urllib.parse.quote('12')  # value1參數值
val2 = urllib.parse.quote('5')

url = (f'https://maker.ifttt.com/trigger/{evt}' +
       f'/with/key/{key}?value1={val1}')

r = req.get(url)  # 執行IFTTT平台的webhooks
#r.text   # 取得IFTTT的回應

print(r.text)
