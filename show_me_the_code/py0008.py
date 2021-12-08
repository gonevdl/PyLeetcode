"""
第 0008 题： 一个HTML文件，找出里面的正文。

第 0009 题： 一个HTML文件，找出里面的链接。
"""

import requests
import re

url = "http://lib.ustc.edu.cn/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36"}

page = requests.get(url, headers=header)

# print(page.text)

obj = re.compile(r'.*?href="(?P<target>.*?)"')
ret = obj.finditer(page.text)
link_list = []
for it in ret:
    link = it.group("target")
    link_list.append(link)

print(link_list)