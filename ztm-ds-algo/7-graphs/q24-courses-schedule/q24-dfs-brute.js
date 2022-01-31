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
// brute solution: DFS start from every nodes

//  1. recursive method:
const hasCycleDFS = function(start, adjList, processed, processing) {
    // this starting node has been processed before -> means already processed all nodes
    // -> means no cycle detected
    if (processed[start]) return false;
    
    // if meet the starting node again in "this round" => cycle detected!!!!!
    if (processing[start]) return true;
    
    processing[start] = true; // in "this round" -> mark the starting node has been traversed 
    const adjs = adjList[start]; 
    for (let i = 0; i < adjs.length; i++) {
        // when the adjacent node detect a cycle
        // -> directly return the result
        if (hasCycleDFS(adjs[i], adjList, processed, processing))
            return true;
    }
     // "this round" is finished
    processing[start] = false; // provide the correct status for the next round
    
    processed[start] = true;  // starting node of this round has been processed
    return false; //this round did not detect cycle
}

var canFinish = function(numCourses, prerequisites) {
    
    const processed = new Array(numCourses);  // to track each starting node process
    const processing = new Array(numCourses); // to track nodes status of each process round
    
    // create adjacency list O(E)
    const adjList = new Array(numCourses).fill(0).map(() => []);
    for (let i = 0; i < prerequisites.length; i++) {
        const edge = prerequisites[i];
        const wantedCourse = edge[0], prereqCourse = edge[1];
        
        adjList[prereqCourse].push(wantedCourse);
    }
    
    // DFS approach to process each node as starting node
    for (let start = 0; start < numCourses; start++) {
        // once a cycle is detected -> means courses cannot be finished
        if(hasCycleDFS(start, adjList, processed, processing))
            return false;
    }
    // after processing every starting nodes and do not detect any cycle
    // -> courses can be finished
    return true
};

// 2. use stack method:
const hasCycleDFS = function (node, adjList, seen) {
    
    const stack = [];
    
    // push the surrounding nodes of the node into the stack
    const surrounding = adjList[node];
    for (let surr of surrounding) {
        stack.push(surr);
    }
    
    // DFS to check it has a cycle or not
    while (stack.length) {
        const curr = stack.pop();
        seen.add(curr)
        // if meet the node again in the process => it has a cycle
        if (curr === node) return true;
        
        const adjacents = adjList[curr];
        for (let adj of adjacents) {
            if (!seen.has(adj))
                stack.push(adj);
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
        // if there is a cycle detected during DFS -> courses can not be finished
        const seen = new Set();
        if (hasCycleDFS(start, adjList, seen)) 
            return false;
    }
    
    // no cycle detected -> able to finish all courses
    return true;
    
};

// time: O(E + V)
// space: O(V^2)

// E: length of prerequisites
// V: number of courses


