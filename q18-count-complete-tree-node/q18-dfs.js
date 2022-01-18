// LeetCode 222.
// https://leetcode.com/problems/count-complete-tree-nodes/

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
 const dfs = function(node, currLevel, height, lastLevelNodes) {
    if(!node) return;
    if(currLevel === height) lastLevelNodes.push(node);
    
    if(node.left) dfs(node.left, currLevel + 1, height, lastLevelNodes);
    if(node.right) dfs(node.right, currLevel + 1, height, lastLevelNodes);
    else return;
}

const calculateHeight = function(root) {
    let temp = root;
    let height = 0;
    while(temp.left) {
        height++;
        temp = temp.left;
    }
    return height;
}

var countNodes = function(root) {
    if(!root) return 0;
    if(root.left === null && root.right === null) return 1;
    
    let count = 0;
    let height = calculateHeight(root);
    count += 2**height - 1;
    
    const lastLevelNodes = []
    dfs(root, 0, height, lastLevelNodes);
    count += lastLevelNodes.length;
    
    return count;
};

// tume: O(n)
// space: O(n)