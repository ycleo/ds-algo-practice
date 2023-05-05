# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 not in nums_set:  # starting sequence
                count = 0
                while n in nums_set:
                    count += 1
                    n += 1
                res = max(res, count)

        return res
# O(N)
# O(N)
