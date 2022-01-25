// LeetCode 200.
// https://leetcode.com/problems/number-of-islands/

/**
 * @param {character[][]} grid
 * @return {number}
 */

// sequential traverse
    // when meet "1" => start BFS, islands++
        // when meet "1" => turn it into "0"
        

const directions = [[-1, 0],  // up => (go -1 in row, 0 in col)
                   [0, 1],   // right => (go 0 in row, 1 in col)
                   [1, 0],   // down => (go 1 in row, 0 in col)
                   [0, -1]]; // left => (go 0 in row, -1 in col)

const bfs = function (row, col, grid) {
    const queue = [[row, col]];
    grid[row][col] = "0";
    
    while (queue.length) {
        const curr = queue.shift();
        const currRow = curr[0], currCol = curr[1];
        
        for (let i = 0; i < directions.length; i++) {
            const dir = directions[i];
            const nextRow = currRow + dir[0], nextCol = currCol + dir[1];
            
            if (nextRow >= 0 && nextRow < grid.length 
                && nextCol >=0 && nextCol < grid[0].length
                && grid[nextRow][nextCol] === "1") {

                grid[nextRow][nextCol] = "0";
                queue.push([nextRow, nextCol]);
            }
        }
    }
};

const numIslands = function(grid) {
    if (grid.length === 0) return 0;
    let islands = 0;
    
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === "1") {
                islands++;
                bfs(i, j, grid);
            }
        }
    }
    return islands;
};

// time: O(m * n)
// space: O(max(m, n))