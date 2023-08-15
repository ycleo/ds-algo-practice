# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        # use the first string to do vertical scan # O( len(shortest string) * len(strs) )
        for i, char in enumerate(prefix):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return prefix[:i]

        return prefix
