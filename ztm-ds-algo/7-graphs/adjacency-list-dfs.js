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

// method 1: using stack
const DFS = function (graph, start) {
    const sequence = [];

    const stack = [start];
    const seen = new Set();

    while (stack.length) {
        const currNode = stack.pop();
        sequence.push(currNode);
        seen.add(currNode);

        const nextNodes = graph[currNode];

        for (let i = 0; i < nextNodes.length; i++) {
            if (!seen.has(nextNodes[i]))
                stack.push(nextNodes[i]);
        }
    }
    return sequence;
}

console.log(DFS(adjacencyList, 7));

// method 2: using recursive
const DFSRecursive = function (graph, node, seen, sequence) {
    sequence.push(node);
    seen.add(node);
    const nextNodes = graph[node];

    for (let i = 0; i < nextNodes.length; i++) {
        if (!seen.has(nextNodes[i])) {
            DFSRecursive(graph, nextNodes[i], seen, sequence);
        }
    }
}

const sequence = [];
DFSRecursive(adjacencyList, 7, new Set(), sequence);
console.log(sequence);