class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProd, minProd = 1, 1
        
        for n in nums:
            newMax, newMin = n * maxProd, n * minProd
            maxProd = max(newMax, newMin, n)
            minProd = min(newMax, newMin, n)
            res = max(res, maxProd)
        
        return res
        
# time: O(n)
# space: O(1)