
// print the 2D array clockwise
const testCase1 = [[ 1,  2,  3, 4], 
                   [12, 13, 14, 5], 
                   [11, 16, 15, 6],
                   [10,  9,  8, 7]];
                  
const testCase2 = [[1, 2], 
                   [6, 3], 
                   [5, 4]];
 
const right = [0, 1], down = [1, 0], left = [0, -1], up = [-1, 0];
 
const print2DArray = function (arr) {
    if (arr.length === 0) return;
    if (arr[0].length === 0) return;
    
    let row = arr.length;
    let col = arr[0].length;
    let count = row * col;
    
    let i = 0, j = 0; // current position
    let dir = right; // current direction
    let step = col;  // how many steps left for this direction
    
    while (count > 0) {
        console.log(arr[i][j]);
        count--;
        step--;
        
        if (step === 0) {
            //going down and touch bottom
            if (dir === down) {
                step = --col;
                dir = left;
            } 
            // going up and touch ceil
            else if (dir === up) {
                step = --col;
                dir = right;
            } 
            // going right and touch right wall
            else if (dir === right) {
                step = --row;
                dir = down;
            } 
            // going left and touch left wall
            else if (dir === left) {
                step = --row;
                dir = up;
            } 
        }
        
        i += dir[0];
        j += dir[1];
    }     
 }

print2DArray(testCase1);
print2DArray(testCase2);
print2DArray([])
 
 // time: O(m * n)
 // space: O(1)
