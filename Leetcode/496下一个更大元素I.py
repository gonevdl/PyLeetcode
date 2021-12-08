"""
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

 

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """找出不同的数组之间的整数的下一个更大的元素"""
        result = []
        for num1 in nums1:
            flag = False
            pos = -1
            for i in range(0, len(nums2)):
                if num1 == nums2[i]:
                    pos = i
            for j in range(pos, len(nums2)):
                if nums2[j] > num1:
                    result.append(nums2[j])
                    flag = True
                    break
            if flag is not True:
                result.append(-1)
        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
