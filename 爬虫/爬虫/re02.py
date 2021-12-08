import re

s = """
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='jolin'><span id='3'>蔡依林</span></div>
<div class='yanzi'><span id='4'>孙燕姿</span></div>
<div class='hh'><span id='5'>佚名</span></div>
"""

# (?P<组名称>)  单独从正则匹配的内容中提取到组的内容，也即是括号里面的正则表达式所匹配的

obj = re.compile(r"div class='.*?'><span id='(?P<id>\d+)'>(?P<want_get>.*?)</span></div>", re.S)  # re.S让.能匹配换行符
ret = obj.finditer(s)
for it in ret:
    print(it.group("id", "want_get"))
