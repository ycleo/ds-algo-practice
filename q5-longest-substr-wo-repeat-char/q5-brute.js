const lengthOfLongestSubstring = function(s) {
    if (s.length <= 1)
        return s.length;
        
    let longest = 0;
    
    for (let i = 0; i< s.length; i++) {
        let seenChars = {};
        let currentLength = 0;
        
        for (let j = i; j < s.length; j++) {
            const char = s[j];
            
            if (!seenChars[char]) {
                currentLength++;
                seenChars[char] = true;
            } else {
                break;
            }
        }
        
        longest = Math.max(longest, currentLength);
    }
    
    return longest;   
};

// time: O(n^2)
// space: O(n)