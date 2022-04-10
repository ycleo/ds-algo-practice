# 1. verify constraints
    # Could s be an empty string? yes, output would be 0

# 2. test cases
    # s = "" -> 0
    # s = "ab" -> 2
    # s = "aaa" -> 1
    # s = "eabcad" -> 4

# 3. algorithm
    # (brute) find every substrings and find the maximum length
    # ex: "abcad" -> "abc", "bcad", "cad", "ad", "d"
    # time: O(n^2), space: O(n)
    
    # (improved) 
    # set longest length = 0, two pointers i = j = 0, hasMap = { char: index }
    # j pointer goes through the s 
        # if (char has repeated) and (is now between i and j)
            # i moves to the hash[char] + 1
        # update hash[char] = j
        # j++
        # check max between (j - i) and longest length
    # return longest length
    
# 4. coding
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)
        
        charMap = {}
        i = j = longestLength = 0
        
        while j < len(s):
            char = s[j]
            if char in charMap and charMap[char] >= i:
                i = charMap[char] + 1
            
            charMap[char] = j
            j += 1
            longestLength = max(longestLength, j - i)
        
        return longestLength
    
# 5. check typo
# 6. run test cases
    
    # s = "eabcad" -> 4 (pass)
        # len(s) = 6
        # longest = 4, map = {e: 0, a: 4, b: 2, c: 3, d: 5}
        # char = d
        # i = 2, j = 6
        
    # s = "" -> 0 (pass)
    # s = "ab" -> 2 (pass)
        # len(s) = 2
        # longest = 2, map = {a: 0, b: 1}
        # char = b
        # i = 0, j = 2
        
    # s = "aaa" -> 1 (pass)
        # len(s) = 3
        # longest = 1, map = {a: 2}
        # char = a
        # i = 2, j = 3

# 7. Analyze complexity
# time: O(n)
# space: O(n)