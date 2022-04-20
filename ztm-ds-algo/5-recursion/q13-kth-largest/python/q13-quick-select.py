# // LeetCode 215.
# // https://leetcode.com/problems/kth-largest-element-in-an-array/

# tail recursion method
def quickSelect(nums, left, right, target):
    if left < right:
        pivot = partition(nums, left, right)
        if pivot == target:
            return
        elif pivot > target:
            quickSelect(nums, left, pivot - 1, target)
        else:
            quickSelect(nums, pivot + 1, right, target)

def partition(nums, left, right):
    pivot = left
    for i in range(left, right):
        if nums[i] < nums[right]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            pivot += 1
    nums[right], nums[pivot] = nums[pivot], nums[right]
    return pivot
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        quickSelect(nums, 0, len(nums) - 1, target)
        return nums[target]


# =========================================================================
# Iterative method

def quickSelect(nums, startIdx, endIdx, position):
    while True:
        pivot, left, right = startIdx, startIdx + 1, endIdx
        while left <= right:
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] <= nums[pivot]:
                left += 1
            if nums[right] >= nums[pivot]:
                right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        
        if right == position:
            return nums[right]
        if right > position:
            endIdx = right - 1
        else:
            startIdx = right + 1
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        position = len(nums) - k
        return quickSelect(nums, 0, len(nums) - 1, position)

# Best, Avg -> time: O(n), space: O(1)
# Worst -> time: O(n ^ 2), space: O(1)