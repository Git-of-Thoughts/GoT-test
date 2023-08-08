from game import Game

def draw_board(game):
    for i in range(game.board_size):
        for j in range(game.board_size):
            if (i, j) in game.snake.get_body():
                print('S', end='')
            elif (i, j) == game.snake.get_head():
                print('H', end='')
            elif (i, j) == game.food.get_position():
                print('F', end='')
            else:
                print('.', end='')
        print()

def get_user_input():
    direction = input('Enter direction (up, down, left, right): ')
    return direction

def main():
    game = Game(10)
    while not game.is_game_over():
        draw_board(game)
        direction = get_user_input()
        game.update(direction)
    print('Game over!')

if __name__ == '__main__':
    main()
