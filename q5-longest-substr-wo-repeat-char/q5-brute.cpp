// LeetCode 3.
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

//Test Cases
    // string s1 = "abcabcbb";  // "abc" or "bca" -> 3
    // string s2 = "bbb";       // "b"   -> 1
    // string s3 = "pwwkew";    // "wke" -> 3
    // string s4 = "";          // ""    -> 0
    // string s5 = "a"          // "a"   -> 1 
    // string s6 = "ab"         // "ab"  -> 2

// "abcabcbb"
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;
        unordered_set<int> temp;
        
        int ans = 0;
        char currTail;
        int currLen;
        
        for (int i = 0; i < s.length() - 1; i++) {
            currLen = 0;
            for (int j = i; j < s.length(); j++) {
                currTail = s[j];
                if(!temp.count(currTail)) {
                    currLen++;
                    temp.insert(currTail);
                } else {
                    break;
                }
            }
            ans = max(ans, currLen);
            temp.clear();
        }
        return ans;
    }
};
// time: O(n^2)
// space: O(n)