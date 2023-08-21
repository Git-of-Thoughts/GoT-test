from snake import Snake
from food import Food

def draw_board(snake, food, board_size):
    for i in range(board_size):
        for j in range(board_size):
            if (i, j) in snake.body:
                print("S", end="")
            elif (i, j) == food.position:
                print("F", end="")
            else:
                print(".", end="")
        print()

def get_user_input():
    direction = input("Enter direction (UP/DOWN/LEFT/RIGHT): ")
    return direction.upper()

def main():
    board_size = 20
    snake = Snake()
    food = Food(board_size)

    while True:
        draw_board(snake, food, board_size)
        direction = get_user_input()
        snake.direction = direction
        snake.move()

        if snake.collided_with_self() or snake.collided_with_wall(board_size):
            print("Game Over!")
            break

        if snake.body[0] == food.position:
            snake.grow()
            food.randomize_position(board_size)

if __name__ == "__main__":
    main()
