"""
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
示例 1：
输入：1
输出：true
示例 2：
输入：10
输出：false

2的幂：1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304
       8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num_str = str(n)
        num_count = len(num_str)
        for i in range(0, 32):
            c_count = self.getDict(i)
            if Counter(num_str) == c_count:
                return True
        return False

    def getDict(self, n: int) -> dict:
        c = str(2 ** n)
        c_count = Counter(c)
        return c_count


num1 = 1
num2 = 4
num3 = 46
num4 = 812
num5 = 1023
print(Solution().reorderedPowerOf2(num1))
print(Solution().reorderedPowerOf2(num2))
print(Solution().reorderedPowerOf2(num3))
print(Solution().reorderedPowerOf2(num4))
print(Solution().reorderedPowerOf2(num5))
