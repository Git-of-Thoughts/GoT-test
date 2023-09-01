#include "solver.cuh"

__global__ void find_best_move_kernel(int* best_move, const int* board) {
    // This kernel will evaluate all possible moves and store the best one in best_move
    // The implementation of this kernel is left as an exercise for the reader
}

int Solver::find_best_move(const TicTacToe& game) {
    int* d_best_move;
    cudaMalloc(&d_best_move, sizeof(int));

    int* d_board;
    cudaMalloc(&d_board, sizeof(int) * 9);
    cudaMemcpy(d_board, game.board, sizeof(int) * 9, cudaMemcpyHostToDevice);

    find_best_move_kernel<<<1, 9>>>(d_best_move, d_board);

    int best_move;
    cudaMemcpy(&best_move, d_best_move, sizeof(int), cudaMemcpyDeviceToHost);

    cudaFree(d_best_move);
    cudaFree(d_board);

    return best_move;
}
