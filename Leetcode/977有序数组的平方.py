"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        length = len(nums)
        pos = self.findzero(nums)
        result = []
        if pos == 0:
            for i in range(0, length):
                result.append(nums[i] ** 2)
                return result
        if pos == (length - 1):
            for i in range(-1, -length - 1, -1):
                result.append(nums[i] ** 2)
                return result
        if nums[pos] >= 0:
            r = pos
            l = pos - 1
        else:
            l = pos
            r = pos + 1
        while (r != length) and (l != -1):
            if nums[r] >= (-nums[l]):
                result.append((-nums[l]) ** 2)
                l -= 1
            else:
                result.append((nums[r]) ** 2)
                r += 1
        for i in range(r, length):
            result.append(nums[r] ** 2)
        for i in range(-1, l, -1):
            result.append((-nums[l]) ** 2)
        return result

    def findzero(self, nums, target=0):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

nums = [1]
print(Solution().sortedSquares(nums))
