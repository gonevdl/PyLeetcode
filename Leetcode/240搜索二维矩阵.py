"""编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def searchMatrix1(self, matrix: list[list[int]], target: int) -> bool:
        if (len(matrix) == 0):
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0 or cols == 0:
            return False
        re_row = 0
        re_col = 0
        for i in range(rows - 1, -1, -1):
            # if (i + rows - cols) < 0:
            #     continue
            if i == 0 or (i + cols - rows) == 0:
                re_row = i
                re_col = i + cols - rows
                break
            if matrix[i][i + cols - rows] >= target:
                re_col = i + cols - rows
                re_row = i
                if i != 0 or (i + cols - rows) != 0:
                    if matrix[i - 1][i - 1 + cols - rows] < target:
                        break
        for i in range(0, re_col + 1):
            if matrix[re_row][i] == target:
                return True
        for i in range(0, re_row + 1):
            temp = matrix[i][re_col]
            if matrix[i][re_col] == target:
                return True
        return False


matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
target = 15
print(Solution().searchMatrix(matrix, target))
