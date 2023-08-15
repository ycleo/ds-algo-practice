# 4, 5, 6, 7, 8, 0, 1, 2
#          m        m      (m is possibly at left or right sprted portion)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # mid is at left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # mid is at right sorted portion: nums[mid] < nums[l]
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1

# time: O(logn)
# space: O(1)