// LeetCode 994.
// https://leetcode.com/problems/rotting-oranges/
/**
 * @param {number[][]} grid
 * @return {number}
 */

// Sequential traverse  
    // know the number of fresh oranges
    // record the position of rotten oranges

// if (fresh == 0) return 0;

// BFS -> check rottens queue is not empty -> update minute
// process rotten oranges:
    // rot adjacent oranges and put into queue
    // decrement fresh number

// if (fresh > 0) return -1
// else return minute

const directions = [ [-1, 0],  // up
                     [1, 0],   // down
                     [0, -1],  // left
                     [0, 1]    //right
                   ];

const checkAround = function (curr, grid) {
    // collect all the surrounding fresh positions
    let fresh = [];
    
    // check the surrounding 4 directions
    for (let i = 0; i < directions.length; i++) {
        
        const dir = directions[i];
        const nextRow = curr[0] + dir[0], nextCol = curr[1] + dir[1];
        
        // check the position is within the grid
        if (nextRow >= 0 && nextRow < grid.length && 
            nextCol >= 0 && nextCol < grid[0].length && 
            grid[nextRow][nextCol] === 1) {

            // collect the position
            fresh.push([nextRow, nextCol]); 
            // turn it into rotten
            grid[nextRow][nextCol] = 2; 
        }
    }
    return fresh;
}

const orangesRotting = function(grid) {
    let minute = 0, fresh = 0, rottens = [];
    
    // traverse the grid to find the fresh number and rotten positions
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === 1) fresh++;
            if (grid[i][j] === 2) rottens.push([i, j]);
        }
    }
    
    // if does not find any fresh orange => answer is 0
    if (fresh === 0) return 0;
    
    // do BFS starting from each rotten orange
    while(rottens.length) {
        /** Key step:
         *  Need to record the number of rottens in the current time, 
         *  so we know when to stop rotting 
         */
        const rotNum = rottens.length;

        for (let i = 0; i < rotNum; i++) {
            
            // get the current rotten position
            const curr = rottens.shift(); 
            
            // find the surrounding fresh oranges and turn them into rotten
            const freshAround = checkAround(curr, grid); 
            fresh -= freshAround.length;
            
            // push their positions into rottens array
            for(let j = 0; j < freshAround.length; j++) {
                rottens.push(freshAround[j]);
            }
        }
        // keep track of time staus
        if (rottens.length) minute++; 
    }
    
    // if some fresh oranges is still not rotten -> answer is -1
    if (fresh > 0) return -1;
    else return minute;
};

// time: O(N)
// space: O(N) if all are rotten