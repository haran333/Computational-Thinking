puzzle = [
        [4,2,9,0,0,1,0,5,8],
        [0,0,8,4,0,9,0,0,2],
        [0,7,0,8,0,3,0,9,0],
        [0,8,0,9,0,0,0,0,3],
        [0,0,3,0,0,0,5,0,0],
        [5,0,0,0,0,2,0,8,0],
        [0,5,0,2,0,7,0,3,0],
        [3,0,0,5,0,4,8,0,0],
        [9,6,0,1,0,0,4,7,5]
    ]

def is_valid(board, row, col, num):
    # col check
    if num in set(board[col]):
        return False

    # row check
    for i in range(9):
        if num == board[i][row]:
            return False

    # 3*3 box check
    boxList = []
    for i in board[3*(col//3): 3*(col//3)+3]:
        boxList += i[3*(row//3): 3*(row//3)+3]
    if num in set(boxList):
        return False

    # num is available
    return True

def solve_sudoku(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:                # target is empty
                for N in range(1, 10):          # input 1~9
                    if is_valid(board, x, y, N):
                        board[y][x] = N
                        if solve_sudoku(board):
                            return True
                        else:
                            board[y][x] = 0
                return False
    return True

def print_board(board):
    print("\n-----Sudoku Answer-----")
    for i in range (9):
        print(*board[i])

if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("풀 수 없는 스도쿠입니다.")