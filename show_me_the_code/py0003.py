"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

count = 0
with open("./src/py0003.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        line_count = line.split(" ")
        count += len(line_count)
        line = f.readline()

print(count)
