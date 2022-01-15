/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

// BFS:
// ans = []
// push the root into Q => Q[root]
// while (Q.length > 0) {    
//     currLen = Q.length
    // for (let i = 0; i < currLen; i++) {
    //     currNode = Q.shift()
    //     if(currNode.left) Q.push(currNode.left)
    //     if(currNode.right) Q.push(currNode.right)
    //     if(i === currLen - 1) ans.push(currNode.val)
    // }
// }
// return ans

const rightSideView = function(root) {
    if(!root) return [];
    
    const ans = [];
    const queue = [root];
    
    while (queue.length) {
        currLen = queue.length;
        for (let i = 0; i < currLen; i++) {
            currNode = queue.shift();
            if(currNode.left) queue.push(currNode.left);
            if(currNode.right) queue.push(currNode.right);
            if(i === currLen - 1) ans.push(currNode.val);
        }
    }
    return ans;
};

// time: O(n)
// space: O(n)