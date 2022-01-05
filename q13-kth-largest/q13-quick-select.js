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

const quickSelect = function(arr, left, right, idxToFind) {
    if (left < right) {
        let partitionIdx = partition(arr, left, right);
        
        if (idxToFind === partitionIdx)
            return;
        else if (idxToFind < partitionIdx)
            return quickSelect(arr, left, partitionIdx - 1, idxToFind);
        else
            return quickSelect(arr, partitionIdx + 1, right, idxToFind);
    }
};

const findKthLargest = function(nums, k) {
    let idxToFind = nums.length - k;
    quickSelect(nums, 0, nums.length - 1, idxToFind);
    return nums[idxToFind];
};


// time: O(n); worst: O(n^2)
// space: O(1) tail recursion