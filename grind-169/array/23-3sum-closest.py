# https://leetcode.com/problems/3sum-closest/
# sorting + two pointers

# target - 3sum = diff
# 3sum = target - diff

# need to find the cloest diff
# diff could be positive or negative -> so need to use abs()

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')

        nums.sort()
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if abs(target - threeSum) < abs(diff):
                    diff = target - threeSum
                if diff == 0:
                    break

                if threeSum < target:
                    l += 1
                else:
                    r -= 1

        return target - diff

# O(N^2)
# O(1)
