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

// courses -> vertex (V)
// prerequisites -> edges (E)
// false conditions -> cyclic 
// brute solution: DFS or BFS start from every nodes
// optimal solution: topological sort

var canFinish = function(numCourses, prerequisites) {
    // edge cases
    if (numCourses < 2 || prerequisites.length < 2) return true;
    
    // create adjacency list and record indegree for each node
    const adjList = new Array(numCourses).fill(0).map(() => []);  
    const inDeg = new Array(numCourses).fill(0);
    for (let i = 0; i < prerequisites.length; i++) {  // O(E)
        const edge = prerequisites[i];
        const wanted = edge[0], prereq = edge[1];
        
        adjList[prereq].push(wanted);
        inDeg[wanted]++;
    }
    
    // create a stack to collect the node whose indegree = 0
    const stack = [];
    // when indegree become 0 => we can remove it from the graph
    // record the removing node number
    let removeCount = 0;
    
    // collect the nodes whose original indegree = 0
    for (let i = 0; i < numCourses; i++) {
        if (inDeg[i] === 0) stack.push(i);
    }
    
    while(stack.length) {  // O(V)
        
        const curr = stack.pop();
        removeCount++;
        
        // get the adjacent nodes of the current node
        const children = adjList[curr];
        for (let i = 0; i < children.length; i++) {  // O(E)
            
            // the current node has been removed from the graph
            // so the indegree of its adjacent node will -1
            const child = children[i];
            inDeg[child]--;
            
            // collect the adjacent nodes whose indegree = 0
            if (inDeg[child] === 0) stack.push(child);
        }
    }
    
    // if we could remove all nodes, we can finish all courses
    return removeCount === numCourses;
};

// time: O(E + V)
// The outer while loop will be executed V number of times 
// and the inner for loop will be executed E number of times.

// space: O(V^2) => also could use edge map instead of adjacent lis
//               => can decrease to O(E or V)

// E: length of prerequisites
// V: number of courses