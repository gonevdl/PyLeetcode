# 密码学作业
a = [3, 3 ** 2, 3 ** 3, 3 ** 4, 3 ** 7]
X = [1] * 32
# print(X)
for i in range(0, len(a)):
    # X[1]=a
    for j in range(1, len(X)):
        X[j] = (a[i] * X[j - 1]) % 31
    # print(X)

# 求Xn+1=(Xn*a)mod2^4的最大周期
a = [i for i in range(1, 2 ** 4)]
X_0 = [i for i in range(1, 2 ** 4)]
result = []
X = []
# print(a)
for a1 in a:
    # X[0]=a1
    for x_0 in X_0:
        X.append(x_0)
        for i in range(1, 18):
            X.append((a1 * X[i - 1]) % (2 ** 4))
            if (X[i] == X[0] and i != 0) or (X[i] == X[i - 1]) or X[i] == 0:
                X[i] = i
                X.append(a1)
                X.append(x_0)
                break
        # print(X)
        result.append(X[:])
        X.clear()

# print(result)
maxn = 0
for nums in result:
    # max=nums[-3]
    if maxn < nums[-3]:
        maxn = nums[-3]
# print(maxn)
for nums in result:
    if nums[-3] == maxn:
        pass
# print(nums)
count = 0
for nums in result:
    if nums[-3] == maxn:
        # print("周期：%d  a:%d  X:%d" % (nums[-3], nums[-2], nums[-1]), end="\t")
        count += 1
    if count == 7:
        # print("")
        count = 0

X = []
for i in range(0, 13):
    X.append(i)
    for j in range(1, 13):
        X.append((X[j - 1] * 6) % 13)
    print(X)
    X.clear()

X = []
for i in range(0, 13):
    X.append(i)
    for j in range(1, 13):
        X.append((X[j - 1] * 7) % 13)
    print(X)
    X.clear()