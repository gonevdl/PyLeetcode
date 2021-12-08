"""
给你一个由 '('、')' 和小写字母组成的字符串 s。
你需要从字符串中删除最少数目的 '(' 或者 ')'（可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
请返回任意一个合法字符串。
有效「括号字符串」应当符合以下任意一条要求：
空字符串或只包含小写字母的字符串
可以被写作AB（A连接B）的字符串，其中A和B都是有效「括号字符串」
可以被写作(A)的字符串，其中A是一个有效的「括号字符串」

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        brackets = []
        if s == "":
            return ""

        for ch in s:
            if "a" <= ch <= "z":
                result.append(ch)
            if ch == "(":
                result.append(ch)
                brackets.append(ch)
            if ch == ")":
                if not brackets:
                    pass
                else:
                    if brackets[-1] != "(":
                        pass
                    else:
                        result.append(")")
                        brackets.pop()

        # 如果栈最后不为空，则说明最后的结果的最右边多出了几个"(",
        # 将这几个"("从结果的尾部删除
        final = "".join(result)
        final = final[::-1]
        if brackets:
            final = final.replace("(", "", len(brackets))
        # print(result)
        return final[::-1]


s = "())()(("
print(Solution().minRemoveToMakeValid(s))
