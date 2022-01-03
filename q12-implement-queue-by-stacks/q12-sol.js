// LeetCode 232.
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    constructor() {
        this.stack1 = [];
        this.stack2 = [];
    }
};

// push(1)
// push(2)
// push(3)
// pop()
// pop()
// push(4)
// pop()
// Q  [2,3]
// S1 []
// S2 [3,2]

// pop() => if s2 is empty, clear out the s1 items into s2

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) { // O(1)
    this.stack1.push(x); 
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {  // O(n)
    if (this.stack2.length === 0) {
        while (this.stack1.length) {
            this.stack2.push(this.stack1.pop());
        }
    }
    return this.stack2.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {  // O(1)
    if (this.stack2.length === 0) return this.stack1[0];
    else return this.stack2[this.stack2.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {   // O(1)
    return (this.stack1.length === 0 && this.stack2.length === 0);
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */