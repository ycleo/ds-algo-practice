# // LeetCode 34.
# // https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def binarySearch(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

class Solution:
    def searchRange(self, nums, target):
        initialIdx = binarySearch(nums, 0, len(nums) - 1, target)
        if initialIdx == -1:
            return [-1, -1]
        
        leftIdx = initialIdx - 1
        rightIdx = initialIdx + 1

        while leftIdx >= 0 and nums[leftIdx] == target:
            leftIdx -= 1
        
        while rightIdx < len(nums) and nums[rightIdx] == target:
            rightIdx += 1
        
        return [leftIdx + 1, rightIdx - 1]

# time: O(n)
# space: O(1)