"""
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，
返回 true ；否则，返回 false 。
示例 1：
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
示例 2：
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
输入：nums = [2,1,5,0,4,6]   3，1，0，4，2，5
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) <= 2:
            return False
        low = 2 ** 31
        mid = 2 ** 32

        for i in range(0, len(nums)):
            if nums[i] <= low:
                low = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            elif nums[i] > mid:
                return True
        return False


nums = [2, 1, 5, 0, 4, 6]
print(Solution().increasingTriplet(nums))
