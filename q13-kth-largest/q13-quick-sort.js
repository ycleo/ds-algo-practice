// LeetCode 215.
// https://leetcode.com/problems/kth-largest-element-in-an-array/

// test cases:
// [5, 6, 4, 2, 3, 1], k = 2   =>  5
// [1, 2, 2, 2, 3, 4], k = 4   =>  2
// [3], k = 1                  =>  3

const partition = function(arr, left, right) {
    let piv = arr[right];
    
    let i = left - 1;
    for (let j = left; j < right; j++) {
        if (arr[j] > piv) {
            i++;
            // swap arr[i] and arr[j]
            let temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    i++;
    
    // swap arr[i] and arr[right]
    let temp = arr[i];
    arr[i] = arr[right];
    arr[right] = temp;
    
    return i;
};

const quickSort = function(arr, left, right) {
    if (left < right) {
        let partitionIdx = partition(arr, left, right);
        
        quickSort(arr, left, partitionIdx - 1);
        quickSort(arr, partitionIdx + 1, right);
    }
};

const findKthLargest = function(nums, k) {
    quickSort(nums, 0, nums.length - 1);
    return nums[k - 1];
};

// time: O(nlogn)
// space: O(logn)