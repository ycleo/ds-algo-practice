const reverseBetween = function(head, m, n) {
    let position = 1;
    let start = cur = head;

    while (position < m) {
        start = cur;
        cur = cur.next;
        position++;
    }

    let reverList = null;
    let tail = cur; // store the tail of the reverse linked list
    
    while (position <= n) {
        // store the next value
        let nxt = cur.next;   

        // add node to the reverList
        cur.next = reverList; 
        reverList = cur;

        cur = nxt;
        position++;
    }

    start.next = reverList;
    tail.next = cur;

    if (m > 1) {  
        return head;
    } else {
        return reverList;
    }

}   

// time: O(n)
// space: O(1)