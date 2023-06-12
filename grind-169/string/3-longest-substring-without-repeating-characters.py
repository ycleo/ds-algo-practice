# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# when the right pointer meets the duplicate (current char)
# if the previous index of current char is "equal or greater than" left pointer
# -> update the left pointer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_to_idx = {}

        l = 0
        for r, c in enumerate(s):
            if c in char_to_idx and char_to_idx[c] >= l:
                l = char_to_idx[c] + 1
            char_to_idx[c] = r
            res = max(res, r - l + 1)

        return res

# O(N)
# O(min(N, k)), k = 26 if consists only lower Engilsh letter
