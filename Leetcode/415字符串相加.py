"""
给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符串转换为整数形式。
示例 1：
输入：num1 = "11", num2 = "123"
输出："134"
示例 2：
输入：num1 = "456", num2 = "77"
输出："533"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        length = min(len2, len1)
        upp = 0
        result = ""
        for i in range(-1, -length - 1, -1):
            sum1 = (ord(num1[i]) + ord(num2[i]) - 2 * ord('0')) + upp
            upp = 0
            if sum1 < 10:
                result += str(sum1)
            else:
                result += str(sum1)[-1]
                upp = 1

        if len1 == len2:
            pass
        elif len1 < len2:
            for i in range(-length - 1, -len2 - 1, -1):
                sum1 = ord(num2[i]) - ord('0') + upp
                upp = 0
                if sum1 < 10:
                    result += str(sum1)
                else:
                    result += str(sum1)[-1]
                    upp = 1
        else:
            for i in range(-length - 1, -len1 - 1, -1):
                sum1 = ord(num1[i]) - ord('0') + upp
                upp = 0
                if sum1 < 10:
                    result += str(sum1)
                else:
                    result += str(sum1)[-1]
                    upp = 1

        if upp == 1:
            result += str(upp)

        result = result[::-1]
        return result


num1 = "11"
num2 = "12"
# 和应为"134"
print(Solution().addStrings(num1, num2))
