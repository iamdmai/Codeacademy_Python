board = [[], [], [], [], []]

def print_board(board):
    for i in range(5):
        board[i].append("O" * 5)

print_board(board)