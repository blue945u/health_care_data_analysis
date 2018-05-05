#透過Python取得該頁資料
#使用requests套件的requests.get()方法
import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
"""
dcard_title = soup.find_all('h3', re.compile('vartitle'))
print('title')
for index, item in enumerate(dcard_title):
    print(item.text.strip().split(' - '))
"""
table = soup.find_all('table')
for item in table[:2]:
    print('--')
    print(item.text.strip())
