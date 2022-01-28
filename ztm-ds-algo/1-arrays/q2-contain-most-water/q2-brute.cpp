// LeetCode 11.
// https://leetcode.com/problems/container-with-most-water/

// Test Cases:
// 1. [1, 8, 2, 3, 7, 2] => 21
// 2. [1, 1] => 1

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int area = 0;

        for (int i = 0; i < height.size() - 1; i++)
        {
            for (int j = i + 1; j < height.size(); j++)
            {
                area = max(area, min(height[i], height[j]) * (j - i));
            }
        }

        return area;
    }
};

// time: O(n^2)
// space: O(1)