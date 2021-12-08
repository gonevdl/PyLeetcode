"""给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:
输入: rowIndex = 3
输出: [1,3,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        # if rowIndex == 1:
        #     return [1]
        yhsj = [[1]]
        for i in range(1, rowIndex + 1):
            temp = []
            for j in range(0, i + 1):
                if j == 0:
                    temp.append(yhsj[i - 1][j])
                elif j == i:
                    temp.append(yhsj[i - 1][j - 1])
                else:
                    temp.append(yhsj[i - 1][j] + yhsj[i - 1][j - 1])
            yhsj.append(temp)
        return yhsj[-1]


s = Solution()
print(s.getRow(3))
