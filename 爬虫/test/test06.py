def hard01(s1: str, s2: str):
    ret = []
    upp = 0
    for i in range(-1, -len(s1) - 1, -1):
        sum1 = ord(s1[i]) - ord("0") + ord(s2[i]) - ord("0") + upp
        if sum1 >= 2:
            ret.append("0")
            upp = 1
        else:
            ret.append(str(sum1))
            upp = 0
    if upp != 0:
        ret.append(str(upp))
    ret.reverse()
    print("".join(ret))


def hard02():
    s = 255
    ret = s & (2 ** 32 - 1)
    sum1 = 0
    b = str(bin(ret))
    for ch in str(bin(ret)):
        if ch == "1":
            sum1 += 1
    return sum1


def hard03():
    s = "my name is Michael, welcome to my "


if __name__ == "__main__":
    # hard01("111", "110")
    print(hard02())
