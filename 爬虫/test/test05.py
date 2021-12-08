"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        sort_s = [0] * 74
        for ch in s:
            sort_s[ord(ch) - ord("0")] += 1
        # sort_s.sort(reverse=True)
        s_dict = {}
        for i in range(0, 68):
            s_dict[i] = sort_s[i]
        ret = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
        s_ret = ""
        for tpl in ret:
            s_ret += chr(tpl[0] + 48) * tpl[1]
        return s_ret


class Solution1:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        length = len(points)
        dictance = []
        for i in range(0, length):
            dist = abs(points[i][0]) ** 2 + abs(points[i][1]) ** 2
            dictance.append([dist, i])
        dictance.sort()
        ret = []
        for i in range(0, k):
            ret.append(points[dictance[i][1]])
        return ret


if __name__ == "__main__":
    s = "tree"
    # print(Solution().frequencySort(s))
    print(Solution1().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
