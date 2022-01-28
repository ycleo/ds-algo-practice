// LeetCode 1376.
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */

// test case:     (1 layer inform time)
//       4        (7)
//     / | \    
//    5  2  6     (3, 4, 6) 
//   /  / \  \
//  7  0   1  3   (5, 0, 0, 0)
// /
//8               (0)

// headID = 4
//  index:    0  1  2  3   4  5  6  7  8
// manager = [2, 2, 4, 6, -1, 4, 4, 5, 7]
// informT = [0, 0, 4, 0,  7, 3, 6, 0, 0] 

// output -> 7 + 3 + 5 + 0 = 15

// map => (manager: subs) => { 4: [2, 5, 6], 5: [7], 2: [0, 1], 6: [3], 7: [8] }

/*
* need to use DFS to know a whole time of certain relationship chains
*/

const DFS = function (ID, informTime, map) {
    // if the inform time is 0, means a leaf node
    // so its actual inform time is 0
    if (informTime[ID] === 0) return 0;
    
    // process the subordinates (children) of the current ID (parent) 
    const subs = map.get(ID);
    
    // the actual inform time of the ID will be
    // 1 layer inform time + Maximum of other subordinates actual inform time
    let maxTime = 0;
    for(let i = 0; i < subs.length; i++) 
        maxTime = Math.max(maxTime, DFS(subs[i], informTime, map));
    
    return informTime[ID] + maxTime;
}


var numOfMinutes = function(n, headID, manager, informTime) {
    if (manager.length <= 1) return 0;
    
    const map = new Map();
    
    // step 1: record the relationship in the map 
    for (let i = 0; i < n; i++) {
        let boss = manager[i];
        if (boss !== -1) {
            if (map.has(boss)) map.get(boss).push(i);
            else map.set(boss, [i]);
        }
    }
    
    // step 2: DFS to find the max time
    return DFS(headID, informTime, map);
};

// time: O(N)
// space: O(N)