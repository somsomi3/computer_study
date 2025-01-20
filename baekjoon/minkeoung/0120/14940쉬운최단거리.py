from collections import deque

# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 테이블 초기화
distance = [[-1] * m for _ in range(n)]

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    # 목표 지점(2)의 위치를 찾기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                start_x, start_y = i, j
                break

    # BFS 초기화
    queue = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0  # 시작 지점 거리 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 유효한 위치인지 확인
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1  # 거리 갱신
                queue.append((nx, ny))

    # 벽(0)은 거리 0으로 설정
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                distance[i][j] = 0

bfs()

# 결과 출력
for row in distance:
    print(' '.join(map(str, row)))