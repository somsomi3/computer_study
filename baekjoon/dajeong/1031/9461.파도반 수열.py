dp = [0, 1, 1, 1, 2, 2] + [0] * 95
for i in range(5, 101):
    dp[i] = dp[i-2] + dp[i-3]

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])