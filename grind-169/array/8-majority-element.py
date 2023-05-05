# https://leetcode.com/problems/majority-element
# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0

        for n in nums:
            if count == 0:
                majority = n
            count += 1 if n == majority else -1

        return majority

# O(n)
# O(1)
