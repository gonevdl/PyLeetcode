from bs4 import BeautifulSoup
import requests
import urllib3

url = "https://www.construdip.com/marketanalysis/0/list/1.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36"
}
urllib3.disable_warnings()
html = requests.get(url, verify=False, headers=header)

print(html.text)

# 1.先从网页生成bs对象
page = BeautifulSoup(html.text, "html.parser")
# 2.从bs中查找数据
# find find_all
# 标签   属性=值
table = page.find("table", attrs={"class": "hq_table"})

tables = table.find_all("tr")[1:]

for t in tables:
    tds = t.find_all("td")
    name = tds[0].text
    print(name)
