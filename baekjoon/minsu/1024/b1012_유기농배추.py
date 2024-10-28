# 유기농 배추

# 방향 - 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS

from collections import deque
q = deque()

def bfs(y, x):
    q.append((y, x))
    while q:
        point = q.popleft()
        for i in range(4):
            ny = point[0] + dy[i]
            nx = point[1] + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if matrix[ny][nx] == 1 and used[ny][nx] == 0:
                used[ny][nx] = 1
                q.append((ny, nx))

T = int(input())
for testcase in range(1, T+1):
    M, N, K = map(int, input().split()) # M : 가로길이 , N : 세로길이 , K : 배추 심긴 위치의 개수
    matrix = [[0] * M for _ in range(N)]
    used = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and used[y][x] == 0:
                count += 1
                bfs(y, x)

    print(count)
