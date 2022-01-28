// LeetCode 98.
// https://leetcode.com/problems/validate-binary-search-tree/

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
 * @return {boolean}
 */
 const compare = function(node, lower, upper) {
    
    if(!node) return true;
    if(node.val > lower && node.val < upper) 
        return compare(node.left, lower, node.val) && compare(node.right, node.val, upper);
    else 
        return false;
}

var isValidBST = function(root) {
    if(!root) return true;
    return compare(root, -Infinity, Infinity);
};

// time: O(n)
// space: O(n)