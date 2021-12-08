"""给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
示例 3：
输入：matrix = [[1]]
输出：[[1]]
示例 4：
输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix
        size = len(matrix)
        result = []
        for i in range(0, size):
            temp = []
            for j in range(size - 1, -1, -1):
                temp.append(matrix[j][i])
            result.append(temp)
        # for i in range(0, size):
        #     for j in range(0, size):
        #         matrix[i][j] = result[i][j]
        # return
        matrix[:] = result


def fun(a, b):
    c = 3
    d = 4
    a = c
    b = d
    # return (a, b)


def fun2(list1):
    list1[0] = 10000


def fun3(str1):
    str1 = str1 + "hello world"


list1 = [1, 2, 3]
print(list1)
fun2(list1)
print(list1)

a = 10
b = 10
print(a, b)
# print(fun(a, b))
fun(a, b)
print(a, b)

str1 = "hello"
print(str1)
fun3(str1)
print(str1)
matrix = [[1, 2], [3, 4]]
print(matrix)
s = Solution()
s.rotate(matrix)
print(matrix)
