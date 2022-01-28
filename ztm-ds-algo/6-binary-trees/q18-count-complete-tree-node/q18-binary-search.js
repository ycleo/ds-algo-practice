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

// 1. edge cases [], [root]
// 2. get tree height h
// 3. count the upper nodes: 2**h - 1
// 4. binary search the last level to find the last node

const nodeExists = function(node, height, idx) {
    let left = 0, right = Math.pow(2, height) - 1, level = 0;
    while(level < height) {
        let mid = Math.ceil((left + right) / 2);
        
        if(idx >= mid) {
            node = node.right;
            left = mid;
        } else {
            node = node.left;
            right = mid - 1;
        }
        level++;
    }
    
    return node !== null;
}

const getHeight = function(root) {
    let temp = root;
    let height = 0;
    while(temp.left) {
        height++;
        temp = temp.left;
    }
    return height;
}

var countNodes = function(root) {
    
    // 1. edge cases
    if(!root) return 0;
    
    // 2. get tree height
    let height = getHeight(root);
    if(height === 0) return 1;
    
    // 3. count upper tree nodes
    let upperCount = Math.pow(2, height) - 1;
    
    // 4. binary search the last level to find the last node
    let left = 0, right = upperCount;
    while(left < right) {
        let mid = Math.ceil((left + right) / 2);
        
        if(nodeExists(root, height, mid)) left = mid;
        else right = mid - 1;
    }
    
    return upperCount + left + 1;
};

// time: O(logN * logN)
// space: O(1)