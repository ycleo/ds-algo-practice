# https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq = collections.Counter(s)
        res = 0
        
        for c in s:
            while char_freq[c] >= 2:
                res += 2
                char_freq[c] -= 2
        
        return res if max(char_freq.values()) == 0 else res + 1
    
# O(n)
# O(n)
                