"""
给定一个整数数组nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
你可以按 任意顺序 返回答案。
进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
示例 1：
输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
示例 2：
输入：nums = [-1,0]
输出：[-1,0]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        count = {}
        result = []
        for i in range(0, len(nums)):
            if count.get(nums[i]) is None:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

            if count[nums[i]] == 2:
                count.pop(nums[i])

        for key in count.keys():
            result.append(key)
        return result


nums = [1, 2, 1, 3, 2, 5]
print(Solution().singleNumber(nums))
