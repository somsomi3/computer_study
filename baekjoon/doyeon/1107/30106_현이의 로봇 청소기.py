import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and abs(arr[nx][ny] - arr[x][y]) <= K:
                    visited[nx][ny] = True
                    dfs(nx, ny)


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            count += 1

print(count)
