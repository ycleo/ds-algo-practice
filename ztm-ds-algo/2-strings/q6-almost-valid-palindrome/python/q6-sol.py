# 1. verify constraints
    # Could s be an empty string? no, length is at least 1
    
# 2. test cases:
    # "a" -> true
    # "aba" -> true
    # "abca" -> true (remove "c")
    # "abc" -> false

# 3. algorithms:
# while i < j
#    "abcbcka"  
#      i   j    
# chars not equal -> split into two situation (i++ or j--)

def isPalindrome(i, j, s: str) -> bool:
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    
class Solution: 
    def validPalindrome(self, s: str) -> bool:

        i = 0 
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i+1, j, s) or isPalindrome(i, j-1, s)
            i += 1
            j -= 1
        return True
    
# time: O(n)
# space: O(1)