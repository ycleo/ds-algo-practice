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
 * @return {number[][]}
 */

// BFS = function(root) {
//     res = []; q = [root];
//     while(q.length) {
//         node = q.dequeue();
//         res.push(node.val);
//         if(node.left) q.enqueue;
//         if(node.right) q.enqueue;
//     }
//     return res;
// }

const levelOrder = function(root) {
    
    if (!root) return [];
    
    const ans = [];
    const queue = [root];
    
    while(queue.length) {
        let temp = [];
        let currLen = queue.length;
        
        for (let j = 0; j < currLen; j++) {
            
            let currNode = queue.shift();
            temp.push(currNode.val);
            
            if(currNode.left) 
                queue.push(currNode.left);
               
            if(currNode.right)
                queue.push(currNode.right);
            
        }
        ans.push(temp);
    }
    return ans;
};

// time: O(n)
// space: O(n)