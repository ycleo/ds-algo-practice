# https://leetcode.com/problems/minimum-window-substring/

# two pointers to track the min window
# use "have" and "need" variables to track the match level
# have = len(countT)

# while have == need -> keep moving the left pointer and check whether it is still match

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        minLength = float("inf")
        start, end = 0, len(s) - 1

        countS, countT = {}, collections.Counter(t)
        have, need = 0, len(countT)

        l = 0
        for r, c in enumerate(s):
            countS[c] = countS.get(c, 0) + 1

            if countS[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start, end = l, r

                if s[l] in countT and countS[s[l]] == countT[s[l]]:
                    have -= 1
                countS[s[l]] -= 1
                l += 1

        return s[start: end + 1] if minLength != float("inf") else ""

# O(N)  N = len(s)
# O(N)
