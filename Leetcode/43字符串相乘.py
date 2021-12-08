"""
给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例2:

输入: num1 = "123", num2 = "456"
输出: "56088"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        upp = 0
        num2_len = len(num2)
        num1_len = len(num1)
        num_2 = 0
        num_1 = 0
        for i in range(-1, -num2_len - 1, -1):
            num_2 += (ord(num2[i]) - ord('0')) * (10 ** (-(i + 1)))
        for i in range(-1, -num1_len - 1, -1):
            num_1 += (ord(num1[i]) - ord('0')) * (10 ** (-(i + 1)))
        result = num_1 * num_2
        return str(result)


num1, num2 = "2", "3"
print(Solution().multiply(num1, num2))
