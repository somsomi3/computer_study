from collections import deque
import sys
input = sys.stdin.readline

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m and not v[ni][nj]:
                if arr[ni][nj]:
                    v[ni][nj] = 1
                    q.append((ni, nj))
                    cnt += 1
    return cnt

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
v = [[0]*m for _ in range(n)]
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            ans = max(ans, bfs(i, j))

print(ans)