# solution1. backtracking + dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set() # contains impossible start indices
        
        def backtrack(idx):
            if idx == len(s):
                return True
            if idx in dp:
                return False
            
            for word in wordDict:
                end = idx + len(word)
                if word == s[idx: end] and backtrack(end):
                        return True
            dp.add(idx)
            return False
                    
        return backtrack(0)
# time: O(s * d * s)
# time: O(s)

# solution 2. bottom-up dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and w == s[i: i + len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

# time: O(s * d * s)
# space: O(s)