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
        
        leftIdx = rightIdx = tmpIdx = initialIdx

        while leftIdx != -1:
            tmpIdx = leftIdx
            leftIdx = binarySearch(nums, 0, leftIdx - 1, target)
        leftIdx = tmpIdx
        
        while rightIdx != -1:
            tmpIdx = rightIdx
            rightIdx = binarySearch(nums, rightIdx + 1, len(nums) - 1, target)
        rightIdx = tmpIdx
        
        return [leftIdx, rightIdx]

# // O( log(n) + log(n/2) + log(n/4) + ... ) = O( log(n) + log(n) + log(n) + ... ) = O(logn)
# // time: O(logn)   
# // space: O(1)