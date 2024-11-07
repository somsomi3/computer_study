from collections import deque

# 입력 받기
N, M, K = map(int, input().split())
arr = [['.'] * M for _ in range(N)]
# 쓰레기 좌표 입력받고 표시
trash = []
for _ in range(K):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = '#'
    trash.append((y - 1, x - 1))
# BFS
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(si, sj):
    queue = deque([(si, sj)])
    # 방문 표시
    visited[si][sj] = True
    # 시작 쓰레기 포함
    count = 1
    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            # 경계를 벗어나지 않고, 방문 안했고, 쓰레기인 경우에 탐색
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count


# 쓰레기 최대 크기 찾기
visited = [[False] * M for _ in range(N)]
max_trash = 0
for x, y in trash:
    if not visited[x][y] and arr[x][y] == '#':
        max_trash = max(max_trash, bfs(x, y))
print(max_trash)