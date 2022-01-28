// LeetCode 11.
// https://leetcode.com/problems/container-with-most-water/

// Test Cases:
// 1. [1, 8, 2, 3, 7, 2] => 21
// 2. [1, 1] => 1

// area = min(height[i], height[j]) * (j - i)

// [1, 8, 2, 3, 7, 2]
//  i              j
// if (height[i] < height[j])
//      i++
// else
//      j--

const maxArea = function(height) {
    let i = 0, j = height.length - 1;
    let area = 0;

    while(i < j) {
        let currArea = Math.min(height[i], height[j]) * (j - i);
        area = Math.max(area, currArea);

        if (height[i] < height[j]) i++;
        else j--;
    }

    return area;
}

// time: O(n)
// space: O(1)