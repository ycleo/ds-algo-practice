// LeetCode 142.
// https://leetcode.com/problems/linked-list-cycle-ii/

const detectCycle = function (head) {
    if (!head) return null;
    
    let tortoise = hare = head;
    while (true) {
        tortoise = tortoise.next;
        hare = hare.next;
        if (!hare) return null;
        hare = hare.next;
        if (!hare) return null;
        if (tortoise === hare) break;
    }

    while (head !== tortoise) {
        head = head.next;
        tortoise = tortoise.next;
    }
    return head;
}

// time: O(n)
// space: O(1)