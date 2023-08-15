# solution 1. (brute)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for s in strs:
            hmap[str(sorted(s))].append(s)
            
        return hmap.values()

# time: O(m * nlog(n))
# space: O(m * n)
# m: length of the strs, n: length of the s

# =====================================================================

# solution 2. (optimize)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
                
            hmap[tuple(count)].append(s)
            
        return hmap.values()

# time: O(m * n)
# space: O(m * n)
# m: length of the strs, n: length of the s