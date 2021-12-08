import os
import time

content = "北京欢迎你，为你开天辟地！"

i = 0
print(content)
while True:
    os.system("cls")
    content = content[1:] + content[0]
    print(content)
    time.sleep(0.3)


