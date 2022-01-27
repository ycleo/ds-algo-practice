const direction = [[-1, 0],  // up => (go -1 in row, 0 in col)
                   [0, 1],   // right => (go 0 in row, 1 in col)
                   [1, 0],   // down => (go 1 in row, 0 in col)
                   [0, -1]]; // left => (go 0 in row, -1 in col)

const bfs = function(matrix, row, col, values, seen) {
    const queue = [[row, col]];
    seen[row][col] = true;
    values.push(matrix[row][col])
    
    while(queue.length) {
        const currPos = queue.shift();
        const currRow = currPos[0];
        const currCol = currPos[1];

        for (let i = 0; i < direction.length; i++) {
            const dir = direction[i];
            const nextRow = currRow + dir[0];
            const nextCol = currCol + dir[1];
            if (nextRow >= 0 && nextRow < matrix.length 
                && nextCol >= 0 && nextCol < matrix[0].length
                && !seen[nextRow][nextCol]) {
                    queue.push([nextRow, nextCol]);
                    seen[nextRow][nextCol] = true;
                    values.push(matrix[nextRow][nextCol]);
                }
        }
    }
}

const traverseBFS = function (matrix) {
    const seen = new Array(matrix.length).fill(0)
                .map(() => new Array(matrix[0].length).fill(false));

    const values = [];  
    bfs(matrix, 0, 0, values, seen);
    return values;         
}

const testMatrix = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
  ];

console.log(traverseBFS(testMatrix));

// time: O(N)
// space: O(N)