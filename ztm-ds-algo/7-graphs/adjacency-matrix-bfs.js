const adjacencyMatrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],  // node 0
    [1, 0, 0, 0, 0, 0, 0, 0, 0],  // node 1
    [0, 0, 0, 1, 0, 0, 0, 0, 1],  // node 2
    [1, 0, 1, 0, 1, 1, 0, 0, 0],  // node 3 
    [0, 0, 0, 1, 0, 0, 1, 0, 0],  // node 4
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  // node 5
    [0, 0, 0, 0, 1, 0, 0, 1, 0],  // node 6
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  // node 7
    [0, 0, 1, 0, 0, 0, 0, 0, 0]   // node 8
]; 
//     0 - 1
//     |
// 5 - 3 - 2 - 8
//     |
//     4 - 6 - 7

const bfs = function (matrix, start) {

    const ans = [];

    // record the node that has been traversed or seen
    const seen = new Set(); 
    // the first row represents the adjacent nodes around the node 0
    const queue = [start];

    while (queue.length) {
        // remove the leftmost node that stay the longest in the queue
        const currNode = queue.shift();
        seen.add(currNode);
        ans.push(currNode);

        // get the number of nodes that surround the current processing node
        const surrNodeNum = matrix[currNode].length;

        for (let i = 0; i < surrNodeNum; i++) {
            if (matrix[currNode][i] == 1 && !seen.has(i)) {
                queue.push(i);
            }
        }
    }
    return ans;
};

console.log(bfs(adjacencyMatrix, 3));

// time: O(N)
// space: O(N)
