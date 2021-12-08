"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os

curDir = os.curdir
# print(curDir)

sourDir = os.path.abspath("..")
# print(sourDir)

sourDir = os.path.join(sourDir, "Leetcode")


def getmylines(sourDir):
    count = 0
    code_count = 0
    ref_count = 0
    blank_count = 0
    code_list = os.listdir(sourDir)
    # print(code_list)
    for mycode in code_list:
        mycode_path = os.path.join(sourDir, mycode)
        with open(mycode_path, "r", encoding="utf-8") as f:
            line = f.readline()
            line = line.strip()
            while line:
                count += 1
                line = f.readline()
                # line = line.strip()
                # print(line)
    return count, code_count, ref_count, blank_count



if __name__ == "__main__":
    lines = getmylines(sourDir)
    print(lines)
