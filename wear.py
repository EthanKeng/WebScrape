import requests
from bs4 import BeautifulSoup
import csv
import random,time
import json
import pandas as pd
import os

if os.path.exists('./wear') == False:
    os.mkdir('./wear')

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
'Referer': 'https://wear.tw/ranking/user/'
}

url = 'https://wear.tw/men-ranking/user/'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
head_shot = soup.find_all('p', class_='item-user-header-avatar')
userUrl_list = []
for i in head_shot:
    userId = i.find('a').get('href')
    userUrl = 'https://wear.tw' + userId
    userUrl_list.append(userUrl)
page=1
for k in userUrl_list:
    pathName = k.split('/')[-2]
    if os.path.exists(f'./wear/{pathName}') == False:
        os.mkdir(f'./wear/{pathName}')

    url = k + f'?pageno={page}'
    for page in range(2):
        resK = requests.get(url, headers=headers)
        soupK = BeautifulSoup(resK.text, 'lxml')
        like_mark = soupK.find_all('li', class_='like_mark')
        for w in like_mark:
            imgUrl = 'https:' + w.find('img').get('data-original')
            print(imgUrl)
            imgPath = f'./wear/{pathName}/' + imgUrl.split('/')[-1]
            try:
                resImg = requests.get(imgUrl, headers=headers)
                with open(imgPath, 'wb') as f:
                    f.write(resImg.content)
                print('done')
            except:
                print('error')    

  

