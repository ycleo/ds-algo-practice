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

const dfs = function (matrix, node, seen, sequence) {
    sequence.push(node);
    seen.add(node);

    const nextNodes = matrix[node];
    for (let i = 0; i < nextNodes.length; i++) {
        if (nextNodes[i] == 1 && !seen.has(i)) {
            dfs(matrix, i, seen, sequence);
        }
    }
}

const sequence = [];
dfs(adjacencyMatrix, 7, new Set(), sequence);
console.log(sequence);

// time: O(N)
// space: O(N)