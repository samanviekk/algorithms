def uniquePaths(row, col):
   # dp = [[1 for _ in range(n)] for i in range(m)]
    dp = [[1] * col for i in range(row)]
    print(dp)

    for i in range(1, row):
        for j in range(1, col):
           dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


    return dp[row-1][col-1]


print(uniquePaths(3, 4))