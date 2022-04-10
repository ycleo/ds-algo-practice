// LeetCode 3.
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

const lengthOfLongestSubstring = function(s) {
    if (s.length <= 1)
        return s.length;

    let longest = 0, i = 0, j = 0;
    let seenChars = {};
    // 1. hash {char: index}
    
    // 2. when j run into the repeat char 
    //    -> check if hash[s[j]] >= i 
    //    -> i move to i = hash[s[j]] + 1 
    
    // 3. update hash[s[j]] = j
    
    while (j < s.length) {
        const char = s[j];
        const seenCharPrevIndex = seenChars[char];
        
        // when the char has repeated "and" is within the current string
        if (seenCharPrevIndex >= i) 
            // update the postition of i
            i = seenCharPrevIndex + 1;
        
        seenChars[char] = j;
        longest = Math.max(longest, j - i + 1);
        j++;
    }
    return longest;
}

// time: O(n)
// space: O(n)