#ifndef SOLVER_CUH
#define SOLVER_CUH

#include "tic_tac_toe.cuh"

class Solver {
public:
    int find_best_move(const TicTacToe& game);
};

#endif
