#ifndef TIC_TAC_TOE_CUH
#define TIC_TAC_TOE_CUH

class TicTacToe {
public:
    TicTacToe();
    void make_move(int move);
    bool is_over() const;
    void print() const;
private:
    int board[3][3];
};

#endif
