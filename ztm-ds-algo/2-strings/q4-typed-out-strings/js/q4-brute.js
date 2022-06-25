// LeetCode 844.
// https://leetcode.com/problems/backspace-string-compare/

const process = (str) => {
    processedStr = []
    for(let i = 0; i < str.length; i++) {
        if (str[i] != '#') 
            processedStr.push(str[i]);
        else if (processedStr.length > 0) 
            processedStr.pop();
    }    
    return processedStr.join('');
}

var backspaceCompare = function(s, t) {
    return process(s) === process(t);
};

// time: O(n + m) 
// space: O(n + m)