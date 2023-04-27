# AABABBA
# l
#    r
# r - l + 1
# maxf + k
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(count.values()) # O(26)
            
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1  
            res = max(res, r - l + 1)
            
        return res

# time: O(n)
# space: O(n)