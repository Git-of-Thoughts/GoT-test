let game = new Game(4);
let gameContainer = document.getElementById('game-container');

// Function to update the game view
function updateGameView() {
  gameContainer.innerHTML = '';
  for (let i = 0; i < game.size; i++) {
    for (let j = 0; j < game.size; j++) {
      let cell = document.createElement('div');
      cell.classList.add('cell');
      cell.innerText = game.grid[i][j] !== 0 ? game.grid[i][j] : '';
      gameContainer.appendChild(cell);
    }
  }
}

// Function to handle key press events
function handleKeyPress(event) {
  if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
    game.playMove(event.key);
    updateGameView();
    if (game.checkGameOver()) {
      alert('Game Over');
    }
  }
}

// Initialize the game view
updateGameView();

// Add key press event listener
document.addEventListener('keydown', handleKeyPress);
