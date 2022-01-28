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

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int i = 0;
        int j = height.size() - 1;
        int area = 0;

        while (i < j)
        {
            area = max(area, min(height[i], height[j]) * (j - i));
            if (height[i] < height[j])
                i++;
            else
                j--;
        }

        return area;
    }
};

// time: O(n)
// space: O(1)