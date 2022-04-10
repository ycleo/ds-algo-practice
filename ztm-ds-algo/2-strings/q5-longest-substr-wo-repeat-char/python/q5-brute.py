# LeetCode 3.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longest = 0
        for i in range(len(s)):
            current_length = 0
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    current_length += 1
            longest = max(longest, current_length)
        return longest

# time: O(n^2)
# space: O(n)
