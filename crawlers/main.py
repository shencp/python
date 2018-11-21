# ------------------------------------------------------------------------------------------------------
# @ get data
import requests

r = requests.get('https://book.douban.com/subject/1084336/comments/')
r.encoding ='utf-8'


# ------------------------------------------------------------------------------------------------------
# @ decode data
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')
for item in pattern:
    print('----')
    print(item.string)

# ------------------------------------------------------------------------------------------------------
# @ save data
import pandas

comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
