class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            other = target - n
            if other in hmap:
                return [hmap[other], i]
            hmap[n] = i


# TC: O(n)
# SC: O(n)
