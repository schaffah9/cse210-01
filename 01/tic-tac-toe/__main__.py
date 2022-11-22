'''
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.
'''

# Global Variables
turn = 0
player = 'X'

board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]

#Functions
def define_turn():
    if turn %2 == 1:
        player = 'X'
    else:
        player = 'O'
    
    return player

def win_condition(player):
    ROW_1 = board[0]
    ROW_2 = board[1]
    ROW_3 = board[2]

    COLUMN_1 = [board[n][0] for n in range(3)]
    COLUMN_2 = [board[n][1] for n in range(3)]
    COLUMN_3 = [board[n][2] for n in range(3)]

    DIAG_1 = [board[n][n] for n in range(3)]
    DIAG_2 = [board[n][2-n] for n in range(3)]

    win_row1 = all(square == player for square in ROW_1)
    win_row2 = all(square == player for square in ROW_2)
    win_row3 = all(square == player for square in ROW_3)
    win_column1 = all(square == player for square in COLUMN_1)
    win_column2 = all(square == player for square in COLUMN_2)
    win_column3 = all(square == player for square in COLUMN_3)
    win_diag1 = all(square == player for square in DIAG_1)
    win_diag2 = all(square == player for square in DIAG_2)

    winners = [
        win_row1, win_row2, win_row3, 
        win_column1, win_column2, win_column3, 
        win_diag1, win_diag2]

    return any(winners)

def check_win():
    return (win_condition('X') or win_condition('O'))

def check_tie():
    is_filled = lambda square : (square == 'X' or square == 'O')
    all_squares = [sq for row in board for sq in row]
    tie_condition = all(map(is_filled, all_squares))
    return tie_condition

def render_board():
    print(f'{board[0][0]}|{board[0][1]}|{board[0][2]}')
    print('-+-+-')
    print(f'{board[1][0]}|{board[1][1]}|{board[1][2]}')
    print('-+-+-')
    print(f'{board[2][0]}|{board[2][1]}|{board[2][2]}')
    print()

def input_move():
    move = input(f'{player}\'s  turn to choose a square (1-9): ')
    print()
    return move

def validate_move(move):
    square_is_valid = move in ['1','2','3','4','5','6','7','8','9']
    square_is_empty = any(move in row for row in board)
    valid = square_is_valid and square_is_empty
    if not valid:
        print('Invalid move. Please try again')
    return valid

def apply_move(move):
    for row in board:
        row[:] = [(player if square == move else square) for square in row]

def main():
    global turn, player, board

    start_turn = True
    render_board()

    while start_turn:
        turn += 1
        player = define_turn()

        is_valid_move = None
        while not is_valid_move:
            move = input_move()
            is_valid_move = validate_move(move)
        apply_move(move)
        
        render_board()

        if check_win():
            start_turn = False
            print(f'{player} has won')
            print('Good game. Thanks for playing!')

        if check_tie():
            start_turn = False
            print('It\'s a tie!')
            print('Good game. Thanks for playing!')

if __name__ == "__main__":
    main()