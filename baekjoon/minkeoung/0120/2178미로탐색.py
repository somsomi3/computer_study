from collections import deque

# 입력 처리
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    while queue:
        x, y = queue.popleft()
        # 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 범위 내이고, 이동 가능한 경로(1)이면서 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 이동 거리 갱신
                queue.append((nx, ny))
    return maze[n - 1][m - 1]  # 도착점 거리 반환

# 결과 출력
print(bfs())