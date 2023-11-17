class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        res = []

        def dfs(idx, currStr):
            if idx == len(s):
                res.append(currStr[:-1])

            string = ""
            curr = trie.root
            for i in range(idx, len(s)):
                if s[i] not in curr.children:
                    return
                curr = curr.children[s[i]]
                string += s[i]
                if curr.isWord:
                    dfs(i+1, currStr + string + ' ')

        dfs(0, "")
        return res

# Time: O (w*k + n^2)  w: len(wordDict), k: max length of word in wordDict, n: len(s)
# Space: O (w*k + n)  w*k: Trie, n: dfs stack

# =========================================================================
# we actually don't need Trie -> we can instead using hashset


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []
        words = set(wordDict)

        def dfs(idx, currStr):
            if idx == n:
                res.append(currStr[:-1])
                return

            string = ""
            for i in range(idx, n):
                string += s[i]
                if string in words:
                    dfs(i+1, currStr + string + ' ')

        dfs(0, "")
        return res
