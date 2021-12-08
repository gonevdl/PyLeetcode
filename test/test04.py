import copy


class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]):
        rectangles.sort()
        i = 1
        length = len(rectangles)
        new_rec = []
        temp = []
        temp.append(rectangles[0])
        new_length = 0
        while i != (length):
            # temp.append(rectangles[i])
            if rectangles[i][0] == rectangles[i - 1][0]:
                temp.append(rectangles[i])
            else:
                #  对temp里面的二维数组按照第二个值的大小排序
                stake = temp[0][0]
                for lst in temp:
                    lst.pop(0)
                temp.sort()
                for lst in temp:
                    lst.insert(0, stake)
                lst_cpy = copy.deepcopy(temp)
                new_rec.append(lst_cpy)
                # new_rec.append([1000000])
                new_length += 1
                temp.clear()
                temp.append(rectangles[i])
            i += 1
        #  再复制一次temp排序算法
        stake = temp[0][0]
        for lst in temp:
            lst.pop(0)
        temp.sort()
        for lst in temp:
            lst.insert(0, stake)
        lst_cpy = copy.deepcopy(temp)
        new_rec.append(lst_cpy)
        # new_rec.append([1000000])
        new_length += 1
        temp.clear()

        #

        # 所围矩形的右边界的一系列的参差不齐的点，这个是随着遍历一直在变化的
        right = []

        # 所围矩形的最大y值，这个值也是确定的
        up = -1000000
        # 所围矩形的最小x值，这个值也是确定的
        left = new_rec[0][0][0]
        # 所围矩形的最小y值，这个值是已经确定的
        down = new_rec[0][0][1]
        temp = new_rec[0]
        for lst in temp:
            if lst[3] > up:
                up = lst[3]
        for col in new_rec:
            for i in range(0, len(col) - 1):
                if (col[i][0] != col[i + 1][0]) or (col[i][3] != col[i + 1][1]):
                    return False


        return new_rec, left, down, new_length


lst = [[1, 3, 1], [1, 1, 1], [2, 2, 2], [3, 6, 3], [3, 3, 3]]
print(Solution().isRectangleCover(lst))
