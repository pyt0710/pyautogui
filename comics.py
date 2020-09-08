from selenium import webdriver


browser = webdriver.ChromeOptions()
browser.add_argument('--headless')
html = webdriver.Chrome(options=browser)
html.get('https://www.manhuabei.com/manhua/haizeiwang/68441.html?p=42')

imgs = html.find_element_by_xpath('//div[@class="chapter-view"]//div[@id="images"]//img').get_attribute("src")
print(imgs)
