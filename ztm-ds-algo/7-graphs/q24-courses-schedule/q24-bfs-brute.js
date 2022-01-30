// LeetCode 207.
// https://leetcode.com/problems/course-schedule/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

// Verify Constraints:
// Can we have courses unconnected with other courses?
//    => Yes, account for seperate course chain

// Write out test cases:
// 1. num = 2, pre = [] => true
// 2. num = 3, pre = [[0, 1], [1, 0]] => false
// 3. num = 5, pre = [[1, 4], [2, 4], [1, 3], [3, 2]] => true

//            0    4 -> 1 <- 3  
//                  \-> 2 ->/ 

// prerequisites -> edges
// false conditions -> cyclic 
// brute solution: DFS or BFS start from every nodes


const hasCycleBFS = function (node, adjList) {
    const seen = new Set();
    const queue = [];
    
    // push the surrounding nodes of the node into the queue
    const surrounding = adjList[node];
    for (let surr of surrounding) {
        queue.push(surr);
    }
    
    // BFS to check it has a cycle or not
    while (queue.length) {
        const curr = queue.shift();
        seen.add(curr)
        // if meet the node again in the process => it has a cycle
        if (curr === node) return true;
        
        const adjacents = adjList[curr];
        for (let adj of adjacents) {
            if (!seen.has(adj))
                queue.push(adj);
        }     
    }
    // no cylce detected
    return false;
}

var canFinish = function(numCourses, prerequisites) {
    if (numCourses < 2 || prerequisites.length < 2) return true;
    
    // create adjancency list
    const adjList = new Array(numCourses).fill(0).map(() => []);
    for (let [wanted, prereq] of prerequisites) 
        adjList[prereq].push(wanted);

    
    // check if there has a cycle start from every nodes
    for (let start = 0; start < numCourses; start++) {
        // if there is a cycle detected during BFS -> courses can not be finished
        if (hasCycleBFS(start, adjList)) 
            return false;
    }
    
    // no cycle detected -> able to finish all courses
    return true;
    
};


// time: O(E + V^3)
// space: O(V^2)

// E: length of prerequisites
// V: number of courses