# ------------------------------------------------------------------------------------------------------
# @ get data
import requests

r = requests.get('https://book.douban.com/subject/1084336/comments/')

# ------------------------------------------------------------------------------------------------------
# @ decode data
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')
for item in pattern:
    print('----')
    print(item.string)
