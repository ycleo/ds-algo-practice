class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curMax = nums[0], 0
        
        for n in nums:
            curMax = max(n, n + curMax)
            res = max(res, curMax)
        
        return res
# O(n)