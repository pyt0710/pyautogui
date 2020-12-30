import requests
import time
from selenium import webdriver


html = webdriver.Chrome()
html.get('https://www.taobao.com')

shoptime = '2020-12-30 20:00:00'

while(True):



    r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
    x = eval(r1.text)
    timeNum = int(x['data']['t'])
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    print(timeArray)

    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

    if otherStyleTime == shoptime:
        print("ok")
        if html.find_element_by_id("J_Go"):
            html.find_element_by_id("J_Go").click()
        if html.find_element_by_link_text('提交订单'):
            html.find_element_by_link_text('提交订单').click()
            break
    
    time.sleep(0.1)
    
