# coding=utf-8

"""
敏感词文本文件 sensitive.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

import os


def isSensitive(youinput):
    curDir = os.curdir
    sensitiveDir = os.path.join(curDir, "src\sensitive.txt")
    sensitive = set()
    with open(sensitiveDir, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        sensitive.add(line)
        while line:
            line = f.readline().strip()
            sensitive.add(line)
    # sensitive_lst = {}  # type: # dict
    youinput_copy = list(youinput)
    for i in range(1, len(youinput) + 1):
        for j in range(0, len(youinput) - i):
            if youinput[j:j + i] in sensitive:
                for k in range(j, j + i):
                    youinput_copy[k] = "*"
    return "".join(youinput_copy)


if __name__ == "__main__":
    your_input = input("输入：")
    print(isSensitive(your_input))
