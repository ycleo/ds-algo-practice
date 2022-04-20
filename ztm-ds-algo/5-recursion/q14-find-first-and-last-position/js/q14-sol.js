// LeetCode 34.
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

// Test Cases:
// [1, 3, 3, 5, 5, 5, 7, 9], target = 5  => [3, 4]
// [1, 3, 5, 7], target = 5 => [3, 3]
// [1, 2, 3, 4], target = 5 => [-1, -1]
// [], target = 5 => [-1, -1]

const searchRange = function(nums, target) {

    let idx = binarySearch(nums, target, 0, nums.length - 1);  
    if (idx === -1) return [-1, -1];
    
    let tempL, tempR;
    let startIdx = idx, endIdx = idx;

    while(startIdx !== -1) {        
        tempL = startIdx;
        startIdx = binarySearch(nums, target, 0, tempL - 1);
    }
    startIdx = tempL;
    
    while(endIdx !== -1) {
        tempR = endIdx;
        endIdx = binarySearch(nums, target, tempR + 1, nums.length - 1);
    }
    endIdx = tempR;
    
    return [startIdx, endIdx];
};

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
// O( log(n) + log(n/2) + log(n/4) + ... ) = O( log(n) + log(n) + log(n) + ... ) = O(logn)
// time: O(logn)   
// space: O(1)