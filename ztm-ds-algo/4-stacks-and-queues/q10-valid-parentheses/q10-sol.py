# LeetCode 20
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in charMap:
                stack.append(char)
            else:
                if len(stack) == 0 or char != charMap[stack.pop()]:
                    return False
        return len(stack) == 0

# time: O(n)
# space: O(n)