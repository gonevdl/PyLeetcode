"""
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。
示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：
输入：s = ")("
输出：[""]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:
    def removeInvalidParentheses(self, s: str):
        s1 = []
        s1[:] = s
        result = []
        size = len(s1)
        for i in range(0, size + 1):
            if s1[i - 1] == "(" or s1[i - 1] == ")":
                temp = []
                temp[:] = s1
                temp2 = []
                if i != 0:
                    temp.pop(i - 1)
                temp2[:] = temp
                # 创建一个栈，用于确定括号匹配
                stack = []
                flag = True
                for ch in temp:
                    if ch == "(":
                        stack.append(ch)
                    elif ch == ")":
                        if stack:
                            if stack[-1] == "(":
                                stack.pop()
                        else:
                            flag = False
                            break
                    else:
                        pass
                if flag is True and len(stack) == 0:
                    # flag3 = True
                    # if temp:
                    #     for ch in temp:
                    #         if ch == "(":
                    #             flag = False
                    # if flag3:
                    temp3 = ""
                    for ch in temp2:
                        temp3 += ch
                    result.append(temp3)
        result.sort()
        result1 = []
        result1[:] = result
        if len(result) == 0:
            flag4 = True
            for ch in s:
                if ch == "(" or ch == ")":
                    flag4 = False
            if flag4:
                result.append(s)
            else:
                result.append("")
            return result
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                result1.pop(i)
        return result1


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lcount, rcount, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove, rremove - 1);
                # 统计当前字符串中已有的括号数量
                if s[i] == ')':
                    lcount += 1
                elif s[i] == ')':
                    rcount += 1
                # 当前右括号的数量大于左括号的数量则为非法,直接返回.
                if rcount > lcount:
                    break

        helper(s, 0, 0, 0, lremove, rremove)
        return res


s = "a"
print(Solution().removeInvalidParentheses(s))
