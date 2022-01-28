// LeetCode 430: 
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

const merge = function (cur) {
    
    let tail = cur.child;
    let nxt = cur.next;

    // find the tail of the child linked list
    while (tail.next) 
        tail = tail.next;
    
    // flatten the tail node    
    tail.next = nxt;
    if (nxt)
        nxt.prev = tail;
    
    // flatten the child node
    cur.next = cur.child;
    cur.next.prev = cur;
    cur.child = null;
}

const flatten = function (head) {
    if (!head) 
        return head;
    
    // Traverse the starting linked list
    let cur = head;
    while (cur) {
        if (!cur.child)
            cur = cur.next;
        else 
            // merge the child linked list
            merge(cur);
    }
    
    return head;
}

// time: O(n)
// space: O(1)