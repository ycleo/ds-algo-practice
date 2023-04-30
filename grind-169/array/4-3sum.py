# https://leetcode.com/problems/3sum/submissions/
# sorting + looping + two pointers !!!

# 1. Sort "nums" -> in order to perform two-pointer search and avoid duplicates

# 2. Iterate through "nums", for each element:
#     - if curr > 0  ->  we cannot form a triplet that sums to zero, so we break out of the loop.
#     - if the curr == prev  -> then skip it to avoid duplicates.
#     - otherwise, two-pointer approach to the pairs that sum up to be = -(curr).

# 3. Return res.

# for two-pointer approach part:
# target = -(curr)
# l, r = i + 1, len(nums) - 1

# While l < r, do the following:
#     Calculate the sum of the numbers at indices l and r.
#     if sum < target -> l++ to increase the next sum
#     if sum > target -> r-- to decrease the next sum
#     if sum == target ->  res.append([-target, nums[l], nums[r]])
#                      ->  l++ to check the next element == prev l or not
#                      ->  If yes, l++ until it's a new number.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            self.twoSum(nums, i)

        return self.res

    def twoSum(self, nums, i):
        target = -nums[i]
        l, r = i + 1, len(nums) - 1

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
