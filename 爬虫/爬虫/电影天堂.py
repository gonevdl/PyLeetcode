import re
import requests
import csv

url = "https://dytt89.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36"
}
html = requests.get(url, verify=False, headers=header)  # verify 去掉安全验证

# 防止乱码，编码方式
html.encoding = 'gb2312'
# print(html.text)

obj = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
ret1 = obj.finditer(html.text)
for it in ret1:
    # global ul
    ul = it.group("ul")
    # print(ul)

    # 拿到ul里面的url

    obj1 = re.compile(r"<li><a href='(?P<target>.*?)' title=", re.S)
    ret2 = obj1.finditer(ul)
    target_list = []

    for it in ret2:
        # print(url + it.group("target").strip("/"))
        target_list.append(url + it.group("target").strip("/"))

    # print(target_list)
    with open("电影天堂2021.csv", "a", encoding='utf-8') as f:
        writer = csv.writer(f)
        for url1 in target_list:
            html = requests.get(url1)
            html.encoding = "gb2312"
            # print(html.text)
            obj2 = re.compile(r'◎片　　名　(?P<title>.*?)<br />.*?'
                              r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<address>.*?)"', re.S)
            ret3 = obj2.search(html.text)
            # print(ret3.group("title", "address"))
            dic = ret3.groupdict()
            writer.writerow(dic.values())
            # break
