// LeetCode 1.
// https://leetcode.com/problems/two-sum/
#include <iostream>
#include <vector>

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ans;
        int com;

        for (int i = 0; i < nums.size(); i++)
        {
            com = target - nums[i];
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (com == nums[j])
                {
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
        return ans;
    }
};

// time: O(n^2)
// space: O(n)