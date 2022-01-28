// LeetCode 104.
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

/**
 * Definition for a binary tree node.
 */
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
 * @return {number}
 */
 const maxDepth = function(root) {
    if (!root) return 0;
    
    let depth = 1;
    depth += Math.max(maxDepth(root.left), maxDepth(root.right));
    
    return depth;
};

// time: O(n)
// space: O(n)   binary tree worst case