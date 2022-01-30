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
// optimal solution: topological sort

var canFinish = function(numCourses, prerequisites) {
    
    // create edges map and record the indegree of each node
    const map = new Map();
    const inDeg = new Array(numCourses).fill(0);
    
    for (let [wanted, prereq] of prerequisites) {
        // record edge relation => worst case space = O(V^2)
        if (map.has(prereq)) map.get(prereq).push(wanted);
        else map.set(prereq, [wanted]);        
        
        // record indegree
        inDeg[wanted]++;
    }
    
    const stack = [];
    let seenCount = 0;
    
    for (let i = 0; i < numCourses; i++) {
        // push the nodes whose indegree is 0 into the stack
        if (inDeg[i] === 0) 
            stack.push(i);
    }
    
    while (stack.length) {  // O(V)
        const curr = stack.pop();
        seenCount++;
        const nexts = map.get(curr)  // worst case of nexts.length = O(V)
        
        if (nexts) {
            for (let next of nexts) {
                inDeg[next]--;
                if (inDeg[next] === 0) stack.push(next);
            }
        }
    }
    
    return seenCount === numCourses;
};

// time: O(E + V^2)
// space: O(V^2)

// E: length of prerequisites
// V: number of courses