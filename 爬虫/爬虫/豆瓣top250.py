import re
import requests
import json
import csv

# 拿到页面源代码
# 使用re提取想要的信息

url = "https://movie.douban.com/top250"
begin = [i * 25 for i in range(0, 19)]
i = 0
for begin_1 in begin:
    para = {
        "start": str(begin_1),
        "filter": ""
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.54 Safari/537.36"
    }
    html = requests.get(url, headers=header, params=para)
    page_content = html.text

    # 解析数据
    obj = re.compile(r'<li>.*?<em class="">(?P<id>\d+)</em>.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?<br>.*?(?P<year>\d+)&nbsp;/&nbsp;.*?<span class="rating_num" '
                     r'property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<persons>.*?)</span>', re.S)

    ret = obj.finditer(page_content)
    with open("豆瓣电影top250.csv", "a", encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        for it in ret:
            # print(it.group("id", "name", "year", "score", "persons"))
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    print("over" + "%d" % i)
    i += 1
