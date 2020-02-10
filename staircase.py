'''def climbStairs(n: int) -> int:
    dp = [0 for index in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
'''
def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0 for index in range(len(cost)]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))