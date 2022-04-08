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
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int sLen = s.length();
        if (sLen <= 1) return sLen;
        
        unordered_map<char, int> hash;
        int ans = 0, i = 0, j = 0;
        char currTail;
    // 1. hash {char: index}
    
    // 2. when j run into the repeated char 
    //    -> check if hash[s[j]] >= i -> i move to i = hash[s[j]] + 1 
    
    // 3. update hash[s[j]] = j
        
        while (j < sLen) {
            currTail = s[j];
            
            // when the char has repeated 
            if (hash.count(currTail)) {
                // when the char is within the current string
                if(hash[currTail] >= i) {
                    i = hash[currTail] + 1;
                }
            } 
                
            hash[currTail] = j;
            ans = max(ans, j - i + 1);
            j++;
            
        }
        return ans;
    }
};

// time: O(n)
// space: O(n)
