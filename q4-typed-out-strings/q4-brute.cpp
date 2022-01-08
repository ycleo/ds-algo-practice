// LeetCode 844.
// https://leetcode.com/problems/backspace-string-compare/

#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string backspace(string s)
    {
        string ans = "";

        for (char c : s)
        {
            if (c == '#')
            {
                if (!ans.empty())
                    ans.pop_back();
            }
            else
            {
                ans.push_back(c);
            }
        }

        return ans;
    }

    bool backspaceCompare(string s, string t)
    {
        return backspace(s) == backspace(t);
    }
};

// time: O(m + n)
// space: O(m + n)