// LeetCode 844.
// https://leetcode.com/problems/backspace-string-compare/

// note: '#' -> pound sign, hash key
//       '*' -> asterisk, star sign

// Test Cases:
// 1. s = "", t = "a#"  -> true
// 2. s = "ab###c#d", t = "a#d"  -> true

// Improved Sol:
#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    bool backspaceCompare(string s, string t) {
        int i = s.length() - 1, j = t.length() - 1;
        int back;
        while (true) {
            // process string s
            back = 0;
            while (i >= 0 && (back > 0 || s[i] == '#')){
                back += (s[i] == '#') ? 1 : -1;
                i--;
            }
            // process string t
            back = 0;
            while (j >= 0 && (back > 0 || t[j] == '#')) {
                back += (t[j] == '#') ? 1 : -1;
                j--;
            }
            // check the current char is equal
            if (i >= 0 && j >=0 && s[i] == t[j]) {
                i--;
                j--;
            } else {
                break;
            }
        }
        return i == -1 && j == -1;
    }
};

// time: O(m + n)
// space: O(1)