# https://leetcode.com/problems/longest-palindromic-substring/
# Expand from the center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(self.res):
                    self.res = s[l: r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i + 1)
            expand(i, i)

        return self.res

# O(n^2)
# O(1)
