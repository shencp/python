# -*- coding:utf-8 -*-
import requests
import pandas as pd
import time
# @ request as
headers = {
    'cookie': '_zap=a63e65c2-984b-4b0a-b3e5-aa6a4b2dfeb1; d_c0="AMAlMgHeWg6PTh0-o6p86K80UdyDTTa8WUI=|1539396163"; capsion_ticket="2|1:0|10:1541333184|14:capsion_ticket|44:OWM1NWI5ZTYyMDMwNDgwODk4NjRjODNmMjc3N2Y4N2E=|32ddec8f1507f3c3f318314f5ef4e5296bcd93dfbc6c451650e17a25b2d482e5"; l_cap_id="NmIwNmFmMTRiMWFkNGJiOTgzNWI5OTI3YWZiYjg4YjM=|1541333311|69829459fa304ff97619b978614bb16c2408c6f5"; r_cap_id="ZDkzYzRkMTQ3YTdkNGQwZjhkZWFmNTM2ODYzZmE3OTQ=|1541333310|eb1402086fa083ac237bddec5ac4876920f13441"; cap_id="Yjg1MjQ2NDBiMTQ3NGJiMDg2NTY3MThjZThhZjgwODM=|1541333310|83ee19baae93cf18c70f42c4e4b9631f663e8f81"; z_c0="2|1:0|10:1541333700|4:z_c0|92:Mi4xQkthOEFRQUFBQUFBd0NVeUFkNWFEaVlBQUFCZ0FsVk54RERNWEFDdFpwaWFBV0E1NkR6MmNCdWFNeU5BdkZQV2lB|41bfc97cda1f079af8be19a98ca460d35e5f86262c04d798613a7d4e4c8465b9"; _xsrf=jnNKg2B3xrsKAi5NTfCfh2j01rtbirSa; q_c1=49c8f0852ad84126ba57c19225c556dc|1542199712000|1539396176000; tst=r; __gads=ID=8059cdda7e906c51:T=1543235675:S=ALNI_MYi-EmS-7Bbb5-Sqf7VJEC0ibINgg; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

import os

os.chdir('C:\\Users\Administrator\Desktop')

user_data = []


# ------------------------------------------------------------------------------------------------------
# @ get data by page
def getDataByPage(pages):
    for page in range(pages):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(
            (page+1) * 20)
        resp = requests.get(url, headers=headers).json()['data']
        user_data.extend(resp)
        print("----page:{}----\n".format(page+1))
        time.sleep(1)


# ------------------------------------------------------------------------------------------------------
# @ main
if __name__ == '__main__':
    getDataByPage(3)
    df = pd.DataFrame.from_dict(user_data)
    df.to_excel('3page.xls')
