"""
给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。
这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。
示例1:
输入: pattern = "abba", str = "dog cat cat dog"  输出: true
示例 2:
输入:pattern = "abba", str = "dog cat cat fish"  输出: false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        pattern_list = pattern[:]
        corr = {}
        if len(s_list) != len(pattern_list):
            return False
        for i in range(0, len(s_list)):
            if pattern_list[i] not in corr:
                if s_list[i] not in corr.values():
                    corr[pattern_list[i]] = s_list[i]
                else:
                    return False
            else:
                if corr[pattern_list[i]] != s_list[i]:
                    return False
        return True


pattern, str1 = "abba", "dog dog dog dog"
print(Solution().wordPattern(pattern, str1))
