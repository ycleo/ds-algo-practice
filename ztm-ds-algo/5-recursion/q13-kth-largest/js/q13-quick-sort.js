// LeetCode 215.
// https://leetcode.com/problems/kth-largest-element-in-an-array/

// - Test Cases:
// [5, 6, 4, 2, 3, 1], k = 2   =>  5
// [1, 2, 2, 2, 3, 4], k = 4   =>  2
// [3], k = 1                  =>  3

// - Quick Sort Solution: divide and conquer => (How to find the partition index)
//                 r
// [5, 6, 4, 2, 1, 3]
//  p
//  i   ->   i
//         (2 < 3)

//                     r
// ["2", 6, 4, "5", 1, 3]
//   p
//              i

//                    r
// [2, "3", 4, 5, 1, "6"]
//     "p"
//             i


// Algorithm:
// qs (nums, 0, nums.len - 1)

// qs (arr, left, right):
//      if (left < right) 
//          p = partition(arr, left, right)
//          qs (arr, left, p-1)
//          qs (arr, p+1, right)

// partition (arr, left, right):
//      p = i = left
//      for i from left to right
//          if (arr[i] < arr[right])
//              swap arr[i] and arr[p]
//              p++
//
//      swap arr[p] and arr[right]
//      return p

const swap = function(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
};

const partition = function(arr, left, right) {
    let piv = arr[right];
    let partitionIdx = left;

    for (let i = left; i < right; i++) {
        if (arr[i] < piv) {
            swap(arr, i, partitionIdx);
            partitionIdx++;
        }    
    }
    
    swap(arr, partitionIdx, right);
    return partitionIdx;
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
    return nums[nums.length - k];
};

// time: O(nlogn); worst: O(n^2)
// space: O(logn)