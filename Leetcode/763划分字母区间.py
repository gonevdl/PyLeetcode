"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]

解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

提示：
S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        s_cpy = s
        interval = []
        while s_cpy != "":
            left = 0
            right = s_cpy.rfind(s_cpy[0])
            temp = s_cpy[left:right + 1]
            new_right = right
            i = 0
            while True:
                end = s_cpy.rfind(temp[i])
                if end > new_right:
                    new_right = end
                temp = s_cpy[left:new_right + 1]
                i += 1
                if i == new_right + 1:
                    break

            right = new_right
            temp = s_cpy[left:right + 1]
            interval.append(temp)
            temp = s_cpy[right + 1:]
            s_cpy = temp

        result = []
        for ch in interval:
            result.append(len(ch))
        return result


S = "qiejxqfnqceocmy"
print(Solution().partitionLabels(S))
