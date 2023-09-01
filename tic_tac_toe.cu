#include "tic_tac_toe.cuh"
#include <iostream>

TicTacToe::TicTacToe() {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            board[i][j] = 0;
        }
    }
}

void TicTacToe::make_move(int move) {
    int row = move / 3;
    int col = move % 3;
    board[row][col] = 1;
}

bool TicTacToe::is_over() const {
    // Check rows, columns, and diagonals for a win
    // This is left as an exercise for the reader
    return false;
}

void TicTacToe::print() const {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cout << board[i][j] << ' ';
        }
        std::cout << '\n';
    }
}
