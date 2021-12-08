"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random


class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums[:]

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        length = len(self.nums)
        result = [0] * length
        rand = random.sample(range(0, length), length)
        for i in range(0, length):
            result[i] = self.nums[rand[i]]
        return result


nums = [1, 2, 3]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.shuffle())
print(obj.shuffle())
