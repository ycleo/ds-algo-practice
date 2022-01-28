
// Prompt: 
// Given a 2D arraycontaining -1's (walls), 0's (gates) and INF's (empty rooms). 
// Fill each empty room with the number of steps to the nearest gate.
// If it is impossible to reach a gate, leave INF as a value.

const I = Infinity;
const wall = -1;
const gate = 0;

testCase1 = [[I, -1, 0,  I], 
             [I,  I, I, -1],
             [I, -1, I, -1], 
             [0, -1, I,  I]]; 

ans1 = [[3, -1, 0,  1],
        [2,  2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3,  4]];

testCase2 = [[ I, -1, 0,  1], 
             [-1,  I, I, -1], 
             [ I, -1, I, -1], 
             [ 0, -1, I,  I]]; 

ans2 =[[ I, -1, 0,  1],
       [-1,  2, 1, -1],
       [ 1, -1, 2, -1],
       [ 0, -1, 3,  4]]; 

// Sequential Traverse to find every gates' position
    // start from each gate do DFS:
        // if next is wall or gate, skip
        // else 
            // step++ (find the smallest steps)

const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

const dfs = function (row, col, step, grid) {
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length ||
        grid[row][col] < step) return;

    grid[row][col] = step;

    for (let i = 0; i < directions.length; i++) {
        const dir = directions[i];
        dfs(row + dir[0], col + dir[1], step + 1, grid);
    }
}

const wallsAndGates = function(grid) {

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] === 0) {
                dfs(row, col, 0, grid);
            }
        }
    }
    return grid;
}

console.log(JSON.stringify(wallsAndGates(testCase1)) === JSON.stringify(ans1));
console.log(JSON.stringify(wallsAndGates(testCase2)) === JSON.stringify(ans2));

// time: O(N)
// space: O(N)