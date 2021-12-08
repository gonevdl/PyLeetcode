# 第一个爬虫程序
from urllib.request import urlopen

url = "https://baidu.com"
resp = urlopen(url)
# print(resp.read().decode("utf-8"))

with open("mybaidu.html", mode="w", encoding='utf-8') as f:
    f.write(resp.read().decode("utf-8"))
print("over")

url2 = "https://jd.com"
resp2 = urlopen(url2)
print(resp2.read().decode("utf-8"))
