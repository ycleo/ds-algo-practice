// LeetCode 1.
// https://leetcode.com/problems/two-sum/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ans;
        unordered_map<int, int> mapping;
        // store {vlue: position}

        for (int i = 0; i < nums.size(); i++)
        {
            int corValue = target - nums[i];

            // if the correndence value exists in the map
            if (mapping.count(corValue))
            {
                ans.push_back(mapping[corValue]);
                ans.push_back(i);
                break;
            }
            mapping[nums[i]] = i;
        }
        return ans;
    }
};

// time: O(n)
// space: O(n)

int main()
{
    vector<int> case1{2, 7, 11, 15};

    Solution sol;
    vector<int> ans = sol.twoSum(case1, 9);

    for (int num : ans)
    {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}