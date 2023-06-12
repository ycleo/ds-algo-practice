# two pointers + keep appending the larger value from the back

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            lv, rv = nums[l]**2, nums[r]**2
            if lv > rv:
                res[i] = lv
                l += 1
            else:
                res[i] = rv
                r -= 1

        return res

# O(N)
# O(N)
