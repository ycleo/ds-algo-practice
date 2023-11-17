# dp[i]: bool whether we can form s[:i]
# recurrence relation:
# dp[i] = for any word in wordDict (dp[i-len(word)] && s[i-len(word):i] == word)
# base case:
# dp[0] = True # s[:0] is empty

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n

        for i in range(1, n+1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
                    break

        return dp[n]

# TC: O(n*w*k) # k: max length of words in wordDict
# SC: O(n)

# =============================================================================
# Word Search Efficiency Optimization => Trie


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, wordDict):
        for word in wordDict:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        trie.buildTrie(wordDict)

        cache = set()  # memorize failed cases

        def dfs(idx):
            if idx == len(s):
                return True
            if idx in cache:
                return False

            curr = trie.root
            for i in range(idx, len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.isWord and dfs(i+1):
                    return True

            cache.add(idx)
            return False

        return dfs(0)


# Time: O (w*k + n^2)  w: len(wordDict), k: max length of word in wordDict, n: len(s)
# Space: O (w*k + n)  w*k: Trie, n: dfs stack
