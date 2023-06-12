# https://leetcode.com/problems/longest-repeating-character-replacement/

# The window size increases only when maxFrequencymaxFrequency finds a new maximum. For this, we always want the following condition to hold true -

# windowSize − maxFrequency <= k
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_map = collections.defaultdict(int)  # char: freq
        maxf = 0

        l = 0
        for r, c in enumerate(s):
            char_map[c] += 1
            maxf = max(maxf, char_map[c])
            while (r - l + 1) - maxf > k:
                char_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# O(n)
# O(26)
