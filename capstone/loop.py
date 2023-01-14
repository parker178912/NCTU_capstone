from selenium import webdriver
import time
import chromedriver_binary

#取得txt檔中水位深度
def waterdepth():
    with open("waterdepth.txt", mode="r") as f:
        r = f.readlines()
        return r[-1]
    
time.sleep(5)
#無限迴圈判斷在水深時發出不同的警報通知
while True:
    browser = webdriver.Chrome()
    msg = int(waterdepth()[0:2])
    if msg <= 20:
            browser.get("https://maker.ifttt.com/trigger/capstone_emergency/with/key/mjT\
            QR0ZnbgiHd2hYBJQSu15o3OpfgsajP8_tsVQMEWw?value1=開始啟動減災措施,請住戶盡速離開")
    elif msg <= 23 and msg > 20:
            browser.get("https://maker.ifttt.com/trigger/capstone_emergency/with/key/mjT\
            QR0ZnbgiHd2hYBJQSu15o3OpfgsajP8_tsVQMEWw?value1=些微淹水,請注意")
    browser.close()
    print(msg)
    time.sleep(5)