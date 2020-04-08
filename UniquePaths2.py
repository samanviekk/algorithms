def uniquePathsWithObstacles(obstacleGrid):
    r = len(obstacleGrid)
    c = len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1: return 0

    dp = [[0] * c for _ in range(r)]
    dp[0][0] = 1
    for j in range(1, c):
        if obstacleGrid[0][j] == 1: break
        dp[0][j] = dp[0][j - 1]

    for i in range(1, r):
        if obstacleGrid[i][0] == 1: break
        dp[i][0] = dp[i - 1][0]

    for i in range(1, r):
        for j in range(1, c):

                if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 0:
                dp[i][j] = dp[i][j - 1]
            if obstacleGrid[i][j - 1] == 1 and obstacleGrid[i - 1][j] == 0:
                dp[i][j] = dp[i - 1][j]
            if obstacleGrid[i][j - 1] == 0 and obstacleGrid[i - 1][j] == 0:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[r - 1][c - 1]

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(uniquePathsWithObstacles(grid))