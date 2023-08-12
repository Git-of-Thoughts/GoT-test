class Game {
  constructor(size = 4) {
    this.size = size;
    this.grid = [...Array(this.size)].map(() => Array(this.size).fill(0));
    this.score = 0;
    this.init();
  }

  // Initialize the game / reset the game
  init() {
    this.grid = [...Array(this.size)].map(() => Array(this.size).fill(0));
    this.addRandomTile();
    this.addRandomTile();
    this.score = 0;
  }

  // Add a new tile in grid at any random empty cell
  addRandomTile() {
    const emptyCells = this.getEmptyCells();
    const randomCell = emptyCells[Math.floor(Math.random() * emptyCells.length)];
    const randomNumber = Math.random() > 0.5 ? 2 : 4;
    this.grid[randomCell[0]][randomCell[1]] = randomNumber;
  }

  // Get all the empty cells
  getEmptyCells() {
    const emptyCells = [];
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (this.grid[i][j] === 0) {
          emptyCells.push([i, j]);
        }
      }
    }
    return emptyCells;
  }

  // Compress the grid after every step before and after merging cells
  compress() {
    // empty grid
    let newGrid = [...Array(this.size)].map(() => Array(this.size).fill(0));

    // here we shift entries of each cell to the extreme left row by row
    for (let i = 0; i < this.size; i++) {
      let pos = 0;

      // traverse the grid
      for (let j = 0; j < this.size; j++) {
        if (this.grid[i][j] !== 0) {
          newGrid[i][pos] = this.grid[i][j];
          pos++;
        }
      }
    }
    this.grid = newGrid;
  }

  // Merge the cells in the grid after compressing
  merge() {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size - 1; j++) {
        // if current cell has same value as next cell and they are non empty then
        if (this.grid[i][j] === this.grid[i][j + 1] && this.grid[i][j] !== 0) {
          // double current cell value and empty the next cell
          this.grid[i][j] = this.grid[i][j] * 2;
          this.grid[i][j + 1] = 0;
          this.score += this.grid[i][j];
        }
      }
    }
  }

  // Reverse the rows (reversing the sequence)
  reverse() {
    for (let i = 0; i < this.size; i++) {
      this.grid[i] = this.grid[i].reverse();
    }
  }

  // Get the transpose of grid
  transpose() {
    let newGrid = this.grid[0].map((_, i) => this.grid.map(row => row[i]));
    this.grid = newGrid;
  }

  // Update the 'score' and 'maxScore' and return the current score
  updateScore() {
    return this.score;
  }

  // Check for game over
  checkGameOver() {
    let spaceAvailable = this.getEmptyCells().length !== 0;
    if (spaceAvailable) {
      return false;
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (i !== this.size - 1 && this.grid[i][j] === this.grid[i + 1][j]) {
          return false;
        }
        if (j !== this.size - 1 && this.grid[i][j] === this.grid[i][j + 1]) {
          return false;
        }
      }
    }
    return true;
  }

  // Check if any moves are possible
  canMove() {
    let previousGrid = JSON.parse(JSON.stringify(this.grid));
    this.compress();
    this.merge();
    this.compress();
    let changedGrid = JSON.parse(JSON.stringify(this.grid));
    this.grid = JSON.parse(JSON.stringify(previousGrid));
    return JSON.stringify(previousGrid) !== JSON.stringify(changedGrid);
  }

  // ArrowUp
  moveUp() {
    // transposing the grid
    this.transpose();
    // compressing the grid
    this.compress();
    // merging the cells
    this.merge();
    // compressing the grid again
    this.compress();
    // transposing the grid back to original state
    this.transpose();
  }

  // ArrowDown
  moveDown() {
    this.transpose();
    this.reverse();
    this.compress();
    this.merge();
    this.compress();
    this.reverse();
    this.transpose();
  }

  // ArrowLeft
  moveLeft() {
    this.compress();
    this.merge();
    this.compress();
  }

  // ArrowRight
  moveRight() {
    this.reverse();
    this.compress();
    this.merge();
    this.compress();
    this.reverse();
  }

  // The action to be taken for each key press
  playMove(direction) {
    if (this.canMove()) {
      if (direction === 'ArrowUp') {
        this.moveUp();
      } else if (direction === 'ArrowDown') {
        this.moveDown();
      } else if (direction === 'ArrowLeft') {
        this.moveLeft();
      } else if (direction === 'ArrowRight') {
        this.moveRight();
      }
      this.addRandomTile();
    }
  }
}
