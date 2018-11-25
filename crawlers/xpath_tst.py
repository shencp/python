# ------------------------------------------------------------------------------------------------------
# @ set work dir
import os

os.chdir('C:\\Users\Administrator\Desktop')
print('------------------------------------------------------------------------------------------')
print(os.getcwd())

from lxml import etree
import requests

# @ with pandas
import pandas as pd

urls = ['https://book.douban.com/subject/1084336/comments/hot?p={}'.format(str(i)) for i in range(1, 10, 1)]

# @ buffer for comments
comment_buffer = []
for url in urls:
    print(url)
    html = requests.get(url)

    print('------------------------------------------------------------------------------------------')
    print('status_code:', html.status_code)

    # @ xpath filter
    s = etree.HTML(html.text)
    comment_list = s.xpath('//div[@class="comment"]/p/span/text()')
    comment_buffer = comment_buffer + comment_list
df = pd.DataFrame(comment_buffer)
df.to_excel('pinglun.xlsx')
