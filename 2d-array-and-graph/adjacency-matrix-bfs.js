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

const bfs = function (matrix) {
    
    const ans = [];
    const seen = new Set(); 

    // the first row represents the adjacent nodes around the node 0
    const queue = [0];

    while (queue.length) {
        const currNode = queue.shift();
        seen.add(currNode);
        ans.push(currNode);
        const surrNodeNum = matrix[currNode].length;

        for (let i = 0; i < surrNodeNum; i++) {
            if (matrix[currNode][i] == 1 && !seen.has(i)) {
                queue.push(i);
            }
        }
    }

    for (let j = 0; j < ans.length; j++) {
        console.log(ans[j]);
    }
};

bfs(adjacencyMatrix);

// time: O(N)
// space: O(N)
