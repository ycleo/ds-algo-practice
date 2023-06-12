# https://leetcode.com/problems/valid-anagram/
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)
        for c in t:
            if c not in s_counter or s_counter[c] == 0:
                return False
            s_counter[c] -= 1

        return True if sum(s_counter.values()) == 0 else False
