"""随机算法"""
# from numpy import random
# import numpy
#
#
# # random.rand()
# def f(x):
#     return (1 - x ** 2) ** 0.5
#
#
# n = 0
# while n != -1:
#     n = int(input("输入n："))
#     k = 0
#     # for i in range(0, n + 1):
#     #     x = random.rand(1)
#     #     print(x)
#     #     break
#     x = random.rand(n)
#     # print(x)
#     y = random.rand(n)
#
#     ret = f(x)
#
#     ret[ret >= y] = 1
#     ret[ret < y] = 0
#     print(sum(ret) / n)
#
# lst = [[5, 109], [3, 9], [19, 10]]
# lst.sort()
# print(lst)

lst = [[0]] * 5
print(lst)

lst[0][0] = 3
print(lst)
