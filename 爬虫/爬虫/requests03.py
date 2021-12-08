import requests
import json

url = "https://movie.douban.com/j/chart/top_list"
# 重新封装参数
parm = {
    'type': "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
response = requests.get(url=url, params=parm, headers=header)
# print(response.request.headers)
# print(response.json())
with open("豆瓣喜剧排行榜.json", "w", encoding='utf-8') as f:
    for dic in response.json():
        f.write(json.dumps(dic, ensure_ascii=False))
        f.write("\n")

# 要关掉response
response.close()
