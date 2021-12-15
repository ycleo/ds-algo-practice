const subIsPalindrome = function(s, p1, p2) {
    while (p1 < p2) {
        if (s[p1] !== s[p2]) return false;
        p1++;
        p2--
    }
    return true;
}

const validPalindrome = function(s) {
    if (s.length <= 1) return true;
    
    //s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
    let p1 = 0, p2 = s.length - 1;
    
    while (p1 <= p2 - 1) {
        if (s[p1] !== s[p2]) {
            return (subIsPalindrome(s, p1+1, p2) || subIsPalindrome(s, p1, p2-1));
        }
        p1++;
        p2--;
    }
    
    return true;
};

// time: O(n)
// space: O(1)