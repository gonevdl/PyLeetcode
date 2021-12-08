"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
示例 1：
输入：nums = [1,1,1], k = 2
输出：2
示例 2：
输入：nums = [1,2,3], k = 3
输出：2
提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# length = len(nums)
# result = 0
# sum_list = []
# for i in range(1, length + 1):
#     window = [0] * i
#     for j in range(0, length - i + 1):
#         window = nums[j:j + i:1]
#         # sum = 0
#         # for num in window:
#         #     sum += num
#         # if sum == k:
#         #     result += 1
#         sum_list.append(window)
# for w in sum_list:
#
# return result

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        length = len(nums)
        sum = 0
        count = 0
        sum_index = []
        for i in range(0, length):
            sum += nums[i]
            sum_index.append(i)
            if sum > k:
                temp = []
                temp[:] = sum_index
                for j in range(0, len(temp)):
                    if sum < k:
                        break
                    sum -= nums[j]
                    sum_index.pop()
                if sum == k:
                    count += 1
            elif sum < k:
                pass
            else:
                count += 1


nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))
