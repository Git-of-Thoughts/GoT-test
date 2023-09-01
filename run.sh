# Compile the code
nvcc -o tic_tac_toe main.cu tic_tac_toe.cu solver.cu

# Run the compiled program
./tic_tac_toe
