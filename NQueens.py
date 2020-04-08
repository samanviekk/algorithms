def solveN_queens(n):
    board = [-1] * n
    res = []
    solveN_queens_helper(board, n, 0,  res)
    return res

def solveN_queens_helper(board, n, row, res):
    if row == n:
        sol = []
        ans = []
        for i, c in enumerate(board):
            dr = ['-'] * n
            dr[board[i]] = "Q"
            ans.append(dr)
        sol.append(ans)
        res.append(sol)
        return
    for col in range(n):
        if is_valid_position(board, n, row, col):
            board[row] = col
            solveN_queens_helper(board, n, row + 1, res)
            board[row] = -1



def is_valid_position(board, n, row, col):
    for r, c in enumerate(board):
        if c == col or row - r == abs(col - c):
            return False
    return True


res = solveN_queens(4)
for sol in res:
    print(sol)




