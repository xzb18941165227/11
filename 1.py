from bs4 import BeautifulSoup
import csv
import requests  # 导入requests库
import os

html_url = ('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4')  # 指定要爬取的url
response = requests.get(html_url)  # 发送get请求
responses=requests.get(html_url)
with open('pc4.html', 'wb') as f:
    f.write(response.content)  # 将爬取到的数据储存到D盘的pc文件夹
    print('完成爬取！！！')
soup=BeautifulSoup(open('pc4.html',encoding='utf-8'),features='html.parser')
print(soup.select('div'))

