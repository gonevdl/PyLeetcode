# 拿到主页面源代码，拿到对应图片的网址

import requests
from bs4 import BeautifulSoup
import time

url = "https://umei.cc/bizhitupian/weimeibizhi/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36"
}

html = requests.get(url, headers=header)
html.encoding = 'utf-8'
# print(html.text)

page = BeautifulSoup(html.text, "html.parser")

a_list = page.find("div", class_="TypeList").find_all("a")
# print(a_list)
for a in a_list:
    # 直接通过get就可以拿到属性的值
    # print("https://umei.cc" + a.get("href"))
    href = "https://umei.cc" + a.get("href")
    href_html = requests.get(href, headers=header)
    href_html.encoding = 'utf-8'
    href_html_text = href_html.text
    target_page = BeautifulSoup(href_html_text, "html.parser")
    p = target_page.find_all("p", attrs={"align": "center"})
    # print(p)
    img = p[0].find("img")
    src = img.get("src")
    name = src.split("/")[-1]
    img_response = requests.get(src)
    with open("img/" + name, "wb") as f:
        f.write(img_response.content)
    # print(target)
    # break
    # time.sleep(1)
    print(name + "over")

print("all over")
