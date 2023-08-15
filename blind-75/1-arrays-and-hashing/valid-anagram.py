# LeetCode 242. https://leetcode.com/problems/valid-anagram/

# test cases:
# s = "a", t = "a"  -> true
# s = "abc", t = "cab" -> true
# s = "ana", t = "an" -> false
# s = "bbb", t = "b" -> false

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = defaultdict(int)
        
        for char in s:
            hmap[char] += 1

        for char in t:
            if char not in hmap:
                return False
            hmap[char] -= 1
        
        for val in hmap.values():
            if val != 0:
                return False
        
        return True
        
# time: O(n)
# space: O(n)