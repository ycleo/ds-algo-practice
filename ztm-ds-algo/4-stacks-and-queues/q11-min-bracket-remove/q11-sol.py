# // LeetCode 1249:
# // https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Algo:
    # leftBracketStack = []
    # s => arr
    # loop through arr:
        # if ( => record index push into stack
        # if ) => if leftStack length > 0 => stack.pop() 
        #      => else arr[now] = ''
        
        # process left bracket if leftStack length > 0
        # return arr -> s'

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sArray = list(s) # O(n)
        
        for i, char in enumerate(sArray): # O(n)
            if sArray[i] == '(':
                stack.append(i)
            if sArray[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    sArray[i] = ''
        
        while len(stack) > 0: # O(n)
            sArray[stack.pop()] = ''
        
        return ''.join(sArray) # O(n)

# time: O(n)
# space: O(n)