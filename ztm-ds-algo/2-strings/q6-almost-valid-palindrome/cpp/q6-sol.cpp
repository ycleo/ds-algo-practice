// LeetCode 680.
// https://leetcode.com/problems/valid-palindrome-ii/

// Test Cases:
// s = "aba" -> true
// s = "raceacar" -> true
// s = "a" -> true
// s = "ab" -> true

// "abxxxfba"
//    i  j
// remove s[i] -> "abxxfba"  if 2nd round s[i] != s[j] -> check the other
//                   i j 
// remove s[j] -> "abxxxba"  --> if still not eaqul -> return false
//                   i j 
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool checkPalindrome(string s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    
    bool validPalindrome(string s) {
        if(s.length() <= 2) return true;
        
        int i = 0, j = s.length() - 1;
        
        string temp = s;
        
        while (i < j) {
            
            if (s[i] != s[j]) {
                return checkPalindrome(s, i + 1, j) || checkPalindrome(s, i, j - 1);
            }
            i++;
            j--;
        }
        
        return true;
    }
};

// time: O(n)
// space: O(1)