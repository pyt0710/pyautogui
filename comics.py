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

print("=" * 100)
print('请输入章节前的数字')
print(chapter)




url = 'https://www.manhuabei.com/manhua/haizeiwang/' + str(input()) + '.html'
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
    
    html.close()
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

def save_img(i):
    
    image = requests.get(title_img[0])
    
    with open(data + '/'+ str(i) + ".jpg",'wb') as f:
        f.write(image.content)
    print('down')
    
i=0
save_img(i)

###############################################################################################
################################################################################
def get_images(url):
    sleep(1)
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    html = webdriver.Chrome(options=browser)
    html.get(url)
   
    imgs = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@id="images"]//img').get_attribute("src")
    print(imgs)
    
    html.close()
    # 图片0，标题1，页码2
    return imgs
url = url+ "?p=" + str(2)


def save_imgs(i):
    image = requests.get(get_images(url))
        
    with open(data + '/'+ str(i) + ".jpg",'wb') as f:
        f.write(image.content)
        print('down')
i=1
i = i + 1
save_imgs(i)


################################################################################


# 获取和保存图片
# 获取章节
# 根据章节内容获取图片
# 自动翻页获取图片

