# https://leetcode.com/problems/3sum/submissions/
# looping + two pointers !!!

# sort the nums
# loop through the nums
# for each iteration:
# if num > 0 -> impossible to form 3 sum (sorted in ascending order) -> end the algo
# if num == prev_num -> skip (continue)

# target = -num
# two pointers technique to find the combination


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            self.twoSum(nums, -n, i + 1, len(nums) - 1)

        return self.res

    def twoSum(self, nums, target, l, r):
        while l < r:
            temp = nums[l] + nums[r]
            if temp < target:
                l += 1
            elif temp > target:
                r -= 1
            else:
                self.res.append([-target, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1


# O(n^2)
# O(1)
