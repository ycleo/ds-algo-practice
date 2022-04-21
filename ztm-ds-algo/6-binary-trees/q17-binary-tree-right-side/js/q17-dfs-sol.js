// LeetCode 199.
// https://leetcode.com/problems/binary-tree-right-side-view/

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

// DFS:
// 1. prioritize the right side
// 2. keep track of the level


// ans = [root.val], maxLevel = 1
// push the root into stack => stack[root]
// stack: [1]
// ans: [1, 3, 4]
// curr = 2; max = 3 

// Sol1:
// const rightSideView = function(root) {
//     if(!root) return [];
    
//     const ans = [root.val];
//     const stack = [root];
//     let maxLevel = 1;
    
//     while (stack.length > 0) { 
//         let currLevel = stack.length + 1
//         currNode = stack[stack.length - 1]
//         if(currLevel > maxLevel) {
//              if (currNode.right) {
//                  stack.push(currNode.right)
//                  ans.push(currNode.right.val)
//                  currNode.right = null
//                  maxLevel = currLevel
//              }
//              else if (currNode.left) {
//                  stack.push(currNode.left)
//                  ans.push(currNode.left.val) 
//                  currNode.left = null
//                  maxLevel = currLevel
//              }
//              else {
//                  stack.pop()
//              }     
//          }
//          else {
//              if (currNode.right) {
//                  stack.push(currNode.right)
//                  currNode.right = null
//              }
//              else if (currNode.left){
//                  stack.push(currNode.left)
//                  currNode.left = null
//              }
//              else {
//                  stack.pop()
//              }     
//          }
//     }
//     return ans
// };

// Sol2:
const dfs = function (node, currLevel, ans) {
    if(!node) return;
    if(currLevel >= ans.length) ans.push(node.val);
    if(node.right) dfs(node.right, currLevel + 1, ans);
    if(node.left) dfs(node.left, currLevel + 1, ans);
}

const rightSideView = function(root) {
    const ans = [];
    dfs(root, 0, ans);
    return ans;
}

// time: O(n)
// space: O(n)
// if it is a complete binary tree => better