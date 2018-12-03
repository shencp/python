# -*- coding:utf-8 -*-
import requests
import time
from pymongo import MongoClient
from fake_useragent import UserAgent

# ------------------------------------------------------------------------------------------------------
client = MongoClient()
db = client.lg
lg_job_set = db.job

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'

headers = {
    'Cookie': 'user_trace_token=20181202194748-3e7943c0-3c7b-4ac2-8a70-84ac5c150c47; LGUID=20181202194751-19614eaa-f628-11e8-891c-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D122.234.64.200; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221676ec22a3446d-0630a50ab13085-6b1b1279-1049088-1676ec22a3528f%22%2C%22%24device_id%22%3A%221676ec22a3446d-0630a50ab13085-6b1b1279-1049088-1676ec22a3528f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _putrc=280DACFE77D69446123F89F2B170EADC; JSESSIONID=ABAAABAAAGGABCB93502C95D3A165B4DBD2CCD26421BE10; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B77547; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=07e66c10fd9b04aba2086ae957a2307daf04d99c67a8af9f4b745401124c93a6; X_HTTP_TOKEN=5460642a5fa2ec419bcc315df85261cb; _gid=GA1.2.490057316.1543840672; _ga=GA1.2.1817578325.1543751271; LGSID=20181203203753-40cd2224-f6f8-11e8-8991-525400f775ce; LGRID=20181203203913-704b6b30-f6f8-11e8-8991-525400f775ce; SEARCH_ID=d58ad986ce0047b5aacca0af4bfdc618; index_location_city=%E6%9D%AD%E5%B7%9E',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


# @ post


# ------------------------------------------------------------------------------------------------------
# @ insert directly


def get_job_info(page_num, kd, url):
    for i in range(page_num):
        form_data = {
            'first': 'true',
            'pn': page_num,
            'kd': kd,
        }

        ua = UserAgent()
        headers['User-Agent'] = ua.random
        response = requests.post(url, data=form_data, headers=headers)

        if response.status_code == 200:
            lg_job_set.insert_many(response.json()['content']['positionResult']['result'])
        else:
            print("----------erro")
        print("-->" + str(i + 1) + "--")
        time.sleep(3)


if __name__=='__main__':
    get_job_info(2, '爬虫',url)
