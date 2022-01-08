// LeetCode 844.
// https://leetcode.com/problems/backspace-string-compare/

// note: '#' -> pound sign, hash key
//       '*' -> asterisk, star sign

const backspaceCompare = function (s, t) {
    let p1 = s.length - 1, p2 = t.length - 1;

    while (p1 >= 0 || p2 >= 0) {
        if (s[p1] === '#' || t[p2] === '#') {
            if (s[p1] === '#') {
                let backCount = 2;
                while (backCount > 0) {
                    backCount--;
                    p1--;

                    if(s[p1] === '#')
                        backCount += 2;
                }
            } 
            if (t[p2] === '#') {
                let backCount = 2;
                while (backCount > 0) {
                    backCount--;
                    p2--;

                    if(t[p2] === '#')
                        backCount += 2;
                }
            }
        } else {
            if (s[p1] !== t[p2]) {
                return false;
            } else {
              p1--;
              p2--;  
            }
        }
    }
    return true;
}

// time: O(n + m)
// space: O(1)