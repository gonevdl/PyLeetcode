class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        count = 0
        dif_s = []
        dif_g = []
        for i in range(0, len(s)):
            if s[i] != goal[i]:
                count += 1
                dif_s.append(s[i])
                dif_g.append(s[i])
                if count > 2:
                    return False
        if count == 1:
            return False
        elif count == 2:
            if sorted(dif_g) == sorted(dif_s):
                return True
            else:
                return False
        else:
            count_lst = [0] * 26
            flag = False
            for i in range(0, 26):
                count_lst[i] = s.count(chr(i + ord("a")))
                if count_lst[i] >= 2:
                    flag = True
            return flag

s = "abcaa"
goal = "abcbb"
print(Solution().buddyStrings(s, goal))