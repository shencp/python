# ------------------------------------------------------------------------------------------------------
# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import re
from pymongo import MongoClient
# ------------------------------------------------------------------------------------------------------

brw = webdriver.Chrome()
wait = WebDriverWait(brw, 10)
client = MongoClient()
taobao_db = client.taobao
taobao_item = taobao_db.item


# @ search shoes by taobao
def search_shoes():
    try:
        brw.get('https://www.taobao.com')
        input_ = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#q")))[0]
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input_.send_keys(u'鞋子')
        submit.click()
        totl=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))[0]
        get_products()
        return totl.text
    except TimeoutException:
        return  search_shoes()

# @ jump the next page
def next_page(page_num):
    try:
        input_ = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))[0]
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input_.clear()
        input_.send_keys(page_num)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_num)))
        get_products()
    except  TimeoutException:
        next_page(page_num)
# @ get taobao products info
def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = brw.page_source
    doc =pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        print(product)
        taobao_item.insert_one(product)
def main():
    tot = search_shoes()
    tot = int(re.compile('(\d+)').search(tot).group(1))
    # @ get total data
    for i in range(2,6):
        next_page(i)

# ------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()





