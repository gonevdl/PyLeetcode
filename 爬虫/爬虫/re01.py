import re

#
# lst = re.findall(r"\d+", "我的电话是10086")
# print(lst)
#
# it = re.finditer(r"\d+", "我的电话是10086")
#
# for i in it:
#     print(i.group())

# search找到一个结果就返回
# s = re.search(r"\d+", "我的电话是10086,她的电话是10010")
# print(s.group())


# 从头开始匹配，默认在正则表达式前面加了个  [^]
s = re.match(r"\d", "10086,她的电话是10010")
print(s.group())

# 预加载正则表达式，将要用的正则表达式先存起来，以后还可以用
obj = re.compile(r'\d+')
ret = obj.finditer("我的电话是10086，10010")
for it in ret:
    print(it.group())
