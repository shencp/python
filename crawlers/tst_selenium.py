# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# ------------------------------------------------------------------------------------------------------
drv = webdriver.Chrome()
drv.get('https://www.baidu.com')
elem = drv.find_element_by_xpath('//*[@id = "kw"]')
elem.send_keys('selenium', Keys.ENTER)
print(drv.page_source)