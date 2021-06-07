# create a tic tac toe board

board = [
    [' ', 'x', ' '],
    ['o', 'x', ' '],
    [' ', ' ', 'o']
]

# print a list inside a list
# print(board[0][1])
# print(board[2][2])

while True:

    row_index = 0
    for row in board:
        col_index = 0
        for col in row:
            if col == ' ':
                print(row_index, col_index, end = ' ')
            else:
                print(col, end = '  ')
            col_index += 1
        print('')
        row_index += 1

    pos_row = int(input('which row?' ))
    pos_col = int(input('which column? '))

    board[pos_row][pos_col] = 'X'



