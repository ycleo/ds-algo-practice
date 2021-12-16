// LeetCode 142.
// https://leetcode.com/problems/linked-list-cycle-ii/

const detectCycle = function (head) {
    if (!head)
        return null;
    
    let cur = head;
    const seenNodes = new Set();
    
    while (!seenNodes.has(cur)) {
        if (!cur.next)
            return null;
        
        seenNodes.add(cur);
        cur = cur.next;
    }
    
    return cur;
};

// time: O(n)
// space: O(n)