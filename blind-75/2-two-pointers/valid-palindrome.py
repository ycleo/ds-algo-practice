class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()

        if len(s) <= 1:
            return True
        
        left, right = 0, len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True

# time: O(n)
# space: O(1)