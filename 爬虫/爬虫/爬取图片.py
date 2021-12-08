# 从花瓣网爬取图片
import requests
import re
import time
import cv2 as cv

url = "https://huaban.com/search/?q=%E5%8A%A8%E6%BC%AB"
child_url = "https://huaban.com/pins/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36"
}
html = requests.get(url=url, headers=header)

# print(html.text)

object = re.compile(r'.*?{"pin_id":(?P<id>.*?),')
ret1 = object.finditer(html.text)

id_list = []
for it in ret1:
    id_img = it.group("id")
    # print(id_img)
    # print(type(id_img))
    # break
    id_list.append(id_img)

# print(id_list)

for i in range(0, len(id_list)):
    if id_list[i][0] == '"':
        temp = ""
        for j in id_list[i]:
            if '0' <= j <= '9':
                temp += j
        id_list.pop(i)
        id_list.append(temp)

# print(id_list)

id_set = set()
for l in id_list:
    if l not in id_set:
        id_set.add(l)

print(id_set)

img_add_set = set()

for img_id in id_set:
    img_url = child_url + img_id + "/"
    img_html = requests.get(url, headers=header)
    object3 = re.compile(r'.*?"key":"(?P<img_key>.*?)"', re.S)
    ret2 = object3.finditer(img_html.text)
    # time.sleep(3)
    for it in ret2:
        temp = it.group("img_key")
        if temp not in img_add_set:
            img_add_set.add(temp)

with open("temp.txt", "w") as f:
    for it in img_add_set:
        f.write(it)
        f.write("\n")
import requests

img_add_set = set()

with open("temp.txt", "r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        img_add_set.add(line)
        line = f.readline()

print(img_add_set)
# result = []
# for ch in img_add_set:
#     ch1 = ch[0:len(ch) - 2]
#     if len(ch) == 52:
#         result.append(ch[0:52])
#
# print(result)

for add in img_add_set:
    furl = "https://hbimg.huabanimg.com/" + add + "_fw658/format/png"
    html = requests.get(furl, headers=header)
    with open("./img/" + add + ".png", "wb") as f:
        f.write(html.content)
    print("图片" + add + ".png写入成功！")
    # cv.imwrite("./img/" + add + ".jpg", html.content)
    # break
    time.sleep(5)
