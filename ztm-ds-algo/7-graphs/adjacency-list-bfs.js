const adjacencyList = [
    [1, 3],
    [0],
    [3, 8],
    [0, 2, 4, 5],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
  ];
//     0 - 1
//     |
// 5 - 3 - 2 - 8
//     |
//     4 - 6 - 7

const bfs =  function (graph, start) {
    const sequence = [];
    const queue = [start];
    const seen = new Set();

    while (queue.length) {
        const currNode = queue.shift();
        sequence.push(currNode);
        seen.add(currNode);
        const surrNodes = graph[currNode];

        for (let i = 0; i < surrNodes.length; i++) {
            if (!seen.has(surrNodes[i])) 
                queue.push(surrNodes[i]);
        }
    }
    return sequence;
};

console.log(bfs(adjacencyList, 3));

// time: O(N)
// space: O(N)