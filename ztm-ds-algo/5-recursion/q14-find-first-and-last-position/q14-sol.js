// LeetCode 34.
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

// Test Cases:
// [1, 3, 3, 5, 5, 5, 7, 9], target = 5  => [3, 4]
// [1, 3, 5, 7], target = 5 => [3, 3]
// [1, 2, 3, 4], target = 5 => [-1, -1]
// [], target = 5 => [-1, -1]

const binarySearch = function(arr, target, left, right) {
    
    while(left <= right) {
        let mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) 
            return mid;      
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    
    return -1;
}

const searchRange = function(nums, target) {
    if(nums.length === 0) return [-1, -1];
    
    let idx = binarySearch(nums, target, 0, nums.length - 1);  
    if (idx === -1) return [-1, -1];
    
    let tempL = idx - 1, tempR = idx + 1;
    
    while(nums[tempL] === target) {        
        tempL = binarySearch(nums, target, 0, tempL) - 1;
    }
    
    while(nums[tempR] === target) {
        tempR = binarySearch(nums, target, tempR, nums.length - 1) + 1;
    }
    
    return [tempL + 1, tempR - 1];
};

// time: O(logn)
// space: O(1)