from selenium import webdriver
import re,os
import requests
from time import sleep


#章节列表
browser = webdriver.ChromeOptions()
browser.add_argument('--headless')
html = webdriver.Chrome(options=browser)
html.get('https://www.manhuabei.com/manhua/haizeiwang.html')
#获取章节
all_chapter = []
for page in html.find_elements_by_xpath('//*[@href]'):
    #print(page.get_attribute('href'),page.get_attribute('title'))
    all_chapter.append(str(page.get_attribute('href')+page.get_attribute('title')))
    
#print(all_chapter)
chapter = re.findall('.*?haizeiwang/(.*?)\..*?html(.*?)\',',str(all_chapter),re.I)
print(chapter)
print("=" * 100)
print('输入章节前的数字')


inint = str(input())
url = 'https://www.manhuabei.com/manhua/haizeiwang/' + inint + '.html'

#获取图片
def get_image(url):
    
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    html = webdriver.Chrome(options=browser)
    html.get(url)

    imgs = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@id="images"]//img').get_attribute("src")
    print(type(imgs))
    title = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@class="head_title"]//h2').text
    print(title)
    
    page = html.find_elements_by_xpath('//div[@class="chapter-view"]//select[@title="page_select"]//option')
    page_number = len(page)
    print(len(page))
    # 图片0，标题1，页码2
    return imgs,title,page_number
#保存图片
title_img = get_image(url)
def create_folder():
    #创建文件夹
    title = title_img[1]
    folder_name = './' + title
    try:
        os.makedirs(folder_name)
    except FileExistsError:
        print('文件夹已存在'+folder_name + '\n' + '不用创建')
    return folder_name
data = create_folder()
def save_img():
    image = requests.get(title_img[0])
    with open(data + '/'+ str(0) + ".jpg",'wb') as f:
        f.write(image.content)
    print('down')
save_img()
sleep(2)

browser = webdriver.ChromeOptions()
browser.add_argument('--headless')
html = webdriver.Chrome(options=browser)
html.get('https://www.baidu.com/')
print('baidu')
def get_images(url):
    html.get(url)
    imgs = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@id="images"]//img').get_attribute("src")
    print(imgs)
    return imgs


def save_imgs(page):
    global url
    global image
    global inint
    url = 'https://www.manhuabei.com/manhua/haizeiwang/' + inint + '.html' + "?p=" + str(page)
    imjpg = get_images(url)
    image = requests.get(imjpg)
        
    with open(data + '/'+ str(page) + ".jpg",'wb') as f:
        f.write(image.content)
        print('down')
page = 2    
num = title_img[2]
while 1:
    if int(page) <= int(num):
        save_imgs(page)    
        page = int(page) + 1
        print(url)
        sleep(1)
    else:
        print('本章节保存完，直接关闭窗口就行')
        break


