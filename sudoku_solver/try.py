






from tkinter import N


example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]


def find_empty_place(example_board):
    # here r = row,c= column
    for r in range(9):
        for c in range(9):
            if example_board[r][c] == -1:
                return r,c
    return None,None



def is_valid(board,guess,row,column):
    # first check row
    row_values = board[row]
    if guess in row_values:
        return False
    
    # second check column values
    column_values = [board[i][column] for i in range(9)]
    if guess in column_values:
        return False
    
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    print("row_start",row_start)
    col_start = (column // 3) * 3
    print("col_start",col_start)
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False
            
    return True
    



def solver(board):
    row, column = find_empty_place(board)
    
    
    if row is None:
        return True
    
    # create guess 1 to 9 using range function
    for guess in range(1, 10):
        if is_valid(board=board,guess=guess,row=row,column=column):
            board[row][column] = guess
            
            if solver(board):
                return True
            
            
        board[row][column] = -1
    return False

print(solver(example_board))