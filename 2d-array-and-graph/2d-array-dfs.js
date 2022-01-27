const direction = [[-1, 0],  // up => (go -1 in row, 0 in col)
                   [0, 1],   // right => (go 0 in row, 1 in col)
                   [1, 0],   // down => (go 1 in row, 0 in col)
                   [0, -1]]; // left => (go 0 in row, -1 in col)

const dfs = function(matrix, row, col, values, seen) {
    if (row < 0 || row >= matrix.length || 
        col < 0 || col >= matrix[0].length ||
        seen[row][col]) {  // remember! seen[row][col] needs to be put at the last
        return; 
    } 

    values.push(matrix[row][col]);
    seen[row][col] = true;

    for (let i = 0; i < direction.length; i++) {
        const dir = direction[i];
        dfs(matrix, row + dir[0], col + dir[1], values, seen);  
    }
}

const traverseDFS = function (matrix) {
    const seen = new Array(matrix.length).fill(0)
                .map(() => new Array(matrix[0].length).fill(false));

    const values = [];  
    dfs(matrix, 0, 0, values, seen);
    return values;         
}

const testMatrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
  ];

console.log(traverseDFS(testMatrix));

// time: O(n)
// space: O(n)