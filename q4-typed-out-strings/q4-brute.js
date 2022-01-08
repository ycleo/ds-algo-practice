// LeetCode 844.
// https://leetcode.com/problems/backspace-string-compare/


const buildStr = function (str) {
    const builtArr = [];

    for (let p = 0; p < str.length; p++) {
        if (str[p] === '#')
            builtArr.pop();
        else
            builtArr.push(str[p]);
    }
    return builtArr;
} 

const backspaceCompare = function (str1, str2) {
    const string1 = buildStr(str1);
    const string2 = buildStr(str2);

    if (string1.length !== string2.length) 
        return false;
    
    for (let p = 0; p < string1.length; p++) {
        if (string1[p] !== string2[p]) 
            return false;
    }

    return true;
}

// time: O(n + m) 
// space: O(n + m)