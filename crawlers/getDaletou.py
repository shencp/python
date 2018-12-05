# coding:utf-8
# ------------------------------------------------------------------------------------------------------
# @ xpath
import requests
from lxml import etree
import time
from scrapy.selector import Selector

# ------------------------------------------------------------------------------------------------------
# @ set work dir
import os

os.chdir('C:\\Users\\15858\Desktop')


# ------------------------------------------------------------------------------------------------------
def getSevenAndThree(url, f, day):
    s = requests.get(url, timeout=20)
    page = etree.HTML(s.text)
    selector = Selector(text=s.text)
    data = selector.xpath('//*[@id="wzxs2_leftb"]/tbody[2]/*/*').xpath('string()').extract()
    i = 0
    for da in data:
        if da == '复式7+3':
            break
        i = i + 1

    print('------------------------------------------------------------------------------------------')
    f.write('\n')
    f.write(day)
    f.write(':')
    f.write(page.xpath('//div[@class="main-hd-article"]/h1[@class="main-hd-title"]/text()')[0])
    f.write('\n------------------------------------------------------------------------------------------\n')
    f.write(data[i])
    f.write(' 【')
    f.write(data[i+1])
    f.write('】 ')
    f.write(data[i+2])
    f.write('\n')


def getSubPageUrl(page_rang):
    for i in range(1, page_rang):
        url = 'https://www.78500.cn/dlt/yc/list-{}.html'.format(str(i))
        r = requests.get(url, timeout=20)
        subpage = etree.HTML(r.text)
        j = 0
        with open('大乐透.txt', 'w', encoding='utf-8') as f:
            for day in subpage.xpath('//*[@class="list-content"]/ul/li/span[@class="d"]/text()'):
                print(day + ":" + subpage.xpath('//*[@class="list-content"]/ul/li/span/a/@href')[j])
                getSevenAndThree(subpage.xpath('//*[@class="list-content"]/ul/li/span/a/@href')[j], f, day)
                j = j + 1

if __name__ == '__main__':
    getSubPageUrl(4)
