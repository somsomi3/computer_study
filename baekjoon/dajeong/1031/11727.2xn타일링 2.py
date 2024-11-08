dp = [0, 1, 3, 5] + [0] * 997

n = int(input())
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n]%10007)