import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
from bs4 import BeautifulSoup


url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response = urllib.request.urlopen(url)
data = response.read().decode()
# print(data)
file_path = "疫情官网.html"
with open(file_path,"w",encoding="utf-8") as f:
    f.write(data))

