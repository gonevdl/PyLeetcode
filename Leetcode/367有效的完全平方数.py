"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如 sqrt 。

示例 1：

输入：num = 16
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = int(num ** 0.5)
        if result ** 2 == num:
            return True
        return False


num1 = 4
num2 = 256
num3 = 2234567890987
print(Solution().isPerfectSquare(num1))
print(Solution().isPerfectSquare(num2))
print(Solution().isPerfectSquare(num3))
