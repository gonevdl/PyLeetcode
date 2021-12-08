import requests

query = input("输入")
url = f"https://www.sogou.com/web?query={query}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36"}
resp = requests.get(url, headers=header)
print(resp.text)
