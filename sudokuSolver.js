// Function to check if a number can be placed at a given position in the Sudoku grid
function isValid(grid, row, col, num) {
    // Check the row
    for(let x = 0; x <= 8; x++) {
        if(grid[row][x] == num) {
            return false;
        }
    }

    // Check the column
    for(let x = 0; x <= 8; x++) {
        if(grid[x][col] == num) {
            return false;
        }
    }

    // Check the 3x3 box
    let startRow = row - row % 3, startCol = col - col % 3;
    for(let i = 0; i < 3; i++) {
        for(let j = 0; j < 3; j++) {
            if(grid[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }

    return true;
}

// Function to solve the Sudoku puzzle using a backtracking algorithm
function solveSudoku(grid, row = 0, col = 0) {
    // If we have reached the 9th row, the Sudoku is solved
    if(row == 9) {
        return true;
    }

    // If the current column is greater than 8, move to the next row
    if(col == 9) {
        return solveSudoku(grid, row + 1, 0);
    }

    // If the current position is filled, move to the next column
    if(grid[row][col] > 0) {
        return solveSudoku(grid, row, col + 1);
    }

    for(let num = 1; num <= 9; num++) {
        // Check if it's safe to place the num (1-9) in the given row and column
        if(isValid(grid, row, col, num)) {
            // Place the num
            grid[row][col] = num;

            // Continue to solve the rest of the grid
            if(solveSudoku(grid, row, col + 1)) {
                return true;
            }
        }

        // If no number can be placed in the current position, backtrack and try the next number
        grid[row][col] = 0;
    }

    return false;
}

// Function to print the solved Sudoku grid
function printGrid(grid) {
    for(let i = 0; i < 9; i++) {
        let row = '';
        for(let j = 0; j < 9; j++) {
            row += grid[i][j] + ' ';
        }
        console.log(row);
    }
}

// Test the Sudoku solver
let grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
];

if(solveSudoku(grid)) {
    printGrid(grid);
} else {
    console.log('No solution exists');
}
