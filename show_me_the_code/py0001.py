"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import random

key_seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0
result = set()
while i < 200:
    temp = ""
    for j in range(1, 26):
        bit = random.randint(0, 61)
        temp += key_seed[bit]
        if (j % 5) == 0 and j != 25 and j != 0:
            temp += "-"
    if temp not in result:
        result.add(temp)
        i += 1
    else:
        pass

print(result)
