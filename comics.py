from selenium import webdriver
import re,os



title = ""
def get_image():
    browser = webdriver.ChromeOptions()
    browser.add_argument('--headless')
    html = webdriver.Chrome(options=browser)
    html.get('https://www.manhuabei.com/manhua/haizeiwang/499917.html')

    imgs = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@id="images"]//img').get_attribute("src")
    print(imgs)
    title = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@class="head_title"]//h2').text
    print(title)
    return title

get_image()


folder_name = title
os.makedirs(folder_name)
