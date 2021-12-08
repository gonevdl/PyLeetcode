# coding=utf-8

"""
敏感词文本文件 sensitive.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

import os


def isSensitive(youinput):
    curDir = os.curdir
    sensitiveDir = os.path.join(curDir, "src/sensitive.txt")
    sensitive = []
    with open(sensitiveDir, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        sensitive.append(line)
        while line:
            line = f.readline().strip()
            sensitive.append(line)
    if youinput in sensitive:
        return True
    else:
        return False


if __name__ == "__main__":
    your_input = input("输入：")
    if isSensitive(your_input):
        print("Freedom")
    else:
        print("Human Rights")
