import requests
import json

url = "https://fanyi.baidu.com/sug"
s = input("输入")
data = {
    "kw": s
}
resp = requests.post(url, data=data)
print(json.loads(resp.text))
