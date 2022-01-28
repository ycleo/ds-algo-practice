// LeetCode 20
// https://leetcode.com/problems/valid-parentheses/

const parens = {
    '{': '}',
    '[': ']',
    '(': ')'
}

const isValid = function(s) {
    
    if(!s) return true;
    
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if(parens[s[i]]) {
            stack.push(s[i]);
        } else {  
            if (s[i] !== parens[stack.pop()]) 
                return false;
        }
    }
    return stack.length === 0;
};

// time: O(n)
// space: O(n)