# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            curr_h = min(height[l], height[r])
            res = max(res, (r - l) * curr_h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

# O(N)
# O(1)
