# https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, p0, p2 = 0, 0, len(nums) - 1

        while p <= p2:
            if nums[p] == 2:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            elif nums[p] == 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
                p += 1
            else:
                p += 1

# Swapping with the leftmost boundary of the 2's could be any of the 3 values, i.e., 0, 1 or even 2. So, we need to process the value at the current index further.
# However, swapping with the rightmost boundary of the 0's could only be 0 -> so p += 1 to skip current index

# O(N)
# O(1)
