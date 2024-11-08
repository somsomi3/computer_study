def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and not v[ni][nj]:
                if abs(arr[ci][cj] - arr[ni][nj]) <= k:
                    q.append((ni, nj))
                    v[ni][nj] = 1

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not v[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)
