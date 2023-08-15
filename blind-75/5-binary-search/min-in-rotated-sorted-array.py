# [1]
# [5, 0]
# [3, 1, 2]
# [3, 4, 5, 1, 2]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
            
        while l <= r:
            
            # already in a fully sorted portion
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # mid is at left sorted portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            # mid is at right sorted portion
            else:
                r = mid - 1
                
        return res

# time: O(logn)
# space: O(1)