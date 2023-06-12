# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Similar methon as LC 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        res = []
        countS, countP = {}, collections.Counter(p)
        have, need = 0, len(countP)

        l = 0
        for r, c in enumerate(s):
            countS[c] = countS.get(c, 0) + 1
            if countS[c] == countP[c]:
                have += 1

            if r >= len(p) - 1:
                if have == need:
                    res.append(l)
                if s[l] in countP and countS[s[l]] == countP[s[l]]:
                    have -= 1
                countS[s[l]] -= 1
                l += 1

        return res

# O(N)  N = len(s)
# O(N)
