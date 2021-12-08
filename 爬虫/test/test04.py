import test03


# 这四个数字能组成多少个互不相同且无重复数字的三位数？
def easy01():
    lst = [3, 6, 2, 7]
    for a in lst:
        for b in lst:
            for c in lst:
                if a not in (b, c) and b != c:
                    print(a, b, c)


# 请写算法，将两个列表交叉相乘，生成如下的矩阵
def easy02():
    lst_1 = [1, 2, 3, 4]
    lst_2 = ['a', 'b', 'c', 'd']
    ret = []
    for a in lst_2:
        temp = []
        for b in lst_1:
            temp.append(f"{b}{a}")
        ret.append(temp)

    print(ret)


# lst = [1,2,3,4,5]，列表向右偏移，两位后，变成lst = [5,4,1,2,3]
def easy03():
    lst = [1, 2, 3, 4, 5]
    ret = lst[-1:-3:-1] + lst[0:3:1]
    print(ret)


# 生成有100个随机正整数的列表，随机数小于1000，遍历列表，删除其中的素数，然后输出最大值，将剩余数值降序输出
import random


def is_prime(num):
    flag = True
    for i in range(2, int(num ** 0.5)):
        if (num // i) * i == num:
            flag = False
            return False
    return True


def easy04():
    lst = [random.randint(0, 999) for i in range(0, 100)]
    print(lst)
    ret = []
    for num in lst:
        if not is_prime(num):
            ret.append(num)
    print(ret)


# 实现算法，查找列表里第二大的数
def easy05():
    lst = [3, 6, 7, 9, 2]
    lst.remove(max(lst))
    print(max(lst))


def is_startswith(source, substr):
    """
    判断字符串source是否以substr开头
    :param source:
    :param substr:
    :return:
    """
    for i in range(0, len(substr)):
        if source[i] != substr[i]:
            return False
    return True


def easy06():
    s = "sdfijer384323js"
    ret = {}
    for ch in s:
        ret.setdefault(ch, 0)
        ret[ch] += 1
    print(ret)


def easy07():
    s1 = "qwertyuiop"
    s2 = "QwertyuiOp"
    if len(s1) != len(s2):
        return False
    for i in range(0, len(s1)):
        if (s1[i] != s2[i]) or (ord(s1[i]) - ord(s2[i]) != 25) or (ord(s1[i]) - ord(s2[i]) != -26):
            return False
    return True


def easy08():
    a = int(input("输入三角形的三边长"))
    b = int(input())
    c = int(input())
    if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
        print("不能构成三角形")
        return
    p = (a + b + c) / 2
    print(a + b + c, (p * (p - a) * (p - b) * (p - c)) ** 0.5)


def easy09(N):
    lst1 = [1]
    lst2 = [1, 1]
    count = 0
    if N == 1:
        print(lst1)
        return
    if N == 2:
        print(lst1)
        print(lst2)
        return
    lst1 = [1]
    # lst2 = []
    print(lst1)
    while count < N - 1:
        lst2 = [0] * (len(lst1) + 1)
        for i in range(0, len(lst1) + 1):
            if i == 0 or i == (len(lst2) - 1):
                lst2[i] = 1
            else:
                lst2[i] = lst1[i] + lst1[i - 1]
        print(lst2)
        lst1 = lst2[:]
        count += 1
    return


# test03

if __name__ == "__main__":
    """调用以上函数"""
    # easy01()
    # easy02()
    # easy03()
    # easy04()
    # easy05()
    # print(is_startswith("python", "pyh"))
    # easy06()
    # print(easy07())
    # easy08()
    easy09(8)
