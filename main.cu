#include <iostream>
#include "tic_tac_toe.cuh"
#include "solver.cuh"

int main() {
    TicTacToe game;
    Solver solver;

    while (true) {
        game.print();
        if (game.is_over()) {
            break;
        }

        int move = solver.find_best_move(game);
        game.make_move(move);
    }

    return 0;
}
