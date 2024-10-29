''''''
# P(N) : N 자리일 때 될 수 있는 여러 값들 중에서 가장 큰 값 한 가지만 정해 출력하기 - DP

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    p = [0] * 5
    p[0] = 1
    p[1] = 1
    p[2] = 1
    p[3] = 2
    p[4] = 2
    if N > 5:
        p += [0 for _ in range(N)]
    for i in range(5, N):
        p[i] = p[i-1] + p[i-5]
    print(p[N-1])


# 1
# 1
# 1
# 2 == (1+1)
# 2
# 3 == (n-1) + (n-5)
# 4 == (n-1) + (n-5)
# 5 == (n-1) +
# 7 == (n-1) + 2
# 9 == (n-1) + 2
# 12 == (n-1) + 3
# 16 == (n-1) + 4
# 21
# 28
#
# P(n) = P(n-1) + P(n-5)