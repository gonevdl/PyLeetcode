"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
https://tieba.baidu.com/p/3691190214?pn=1
"""

import requests
import re
import os
import time

curDir = os.curdir
desDir = os.path.join(curDir, r"src\ChinesePhoto")
print(desDir)
# 网址
url = "https://tieba.baidu.com/p/3691190214?pn="
maxPage = 25
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/96.0.4664.45 Safari/537.36"
}
# 匹配正则表达式
obj = re.compile(r'.*?<img class="BDE_Image".*?" src="(?P<img_url>.*?)" pic_ext="')

count = 16
# 获取网页，网页一共有25页
for i in range(2, maxPage + 1):
    page = requests.get(url + "i", headers=header)
    # 拿到所有的匹配的正则表达式
    img_iter = obj.finditer(page.text)
    img_list = []
    for it in img_iter:
        img_url = it.group("img_url")
        img_list.append(img_url)
    # print(img_list)
    # print(len(img_list))
    # break
    # img_list中存储所有的图片的链接
    for img_u in img_list:
        img_page = requests.get(img_u, headers=header)
        time.sleep(3)
        name = str(count) + ".jpg"
        # print(name)
        with open(os.path.join(desDir, name), "wb") as f:
            f.write(img_page.content)
            print("%s写入成功！" % name)
        count += 1
    time.sleep(5)
    # break
