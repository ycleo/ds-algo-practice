# https://leetcode.com/problems/move-zeroes/solution/

# l moves with r or points to the first 0 value
# if r != 0 -> swap and both move forward
# else -> only r
#  move forward


#    l
# 1, 0, 0, 3, 12
#          r

#       l
# 1, 3, 0, 0, 12
#              r

# 1, 3, 12, 0, 0


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
# O(n)
# O(1)
