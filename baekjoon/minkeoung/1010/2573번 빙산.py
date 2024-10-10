import sys
from collections import deque

# 상, 하, 좌, 우 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 빙산의 연결된 덩어리 탐색
def bfs(x, y, visited, iceberg, n, m):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and iceberg[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 빙산 녹이기
def melt_iceberg(iceberg, n, m):
    melt = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if iceberg[x][y] > 0:
                sea_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] == 0:
                        sea_count += 1
                melt[x][y] = sea_count

    for x in range(n):
        for y in range(m):
            iceberg[x][y] = max(0, iceberg[x][y] - melt[x][y])

# 빙산 덩어리 수 계산
def count_icebergs(iceberg, n, m):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(m):
            if iceberg[x][y] > 0 and not visited[x][y]:
                bfs(x, y, visited, iceberg, n, m)
                count += 1

    return count

# 메인 함수
def solution():
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    iceberg = [list(map(int, data[i + 1].split())) for i in range(n)]

    year = 0

    while True:
        icebergs = count_icebergs(iceberg, n, m)

        if icebergs >= 2:  # 빙산이 두 덩어리 이상으로 분리된 경우
            print(year)
            return

        if icebergs == 0:  # 빙산이 모두 녹아 덩어리가 없는 경우
            print(0)
            return

        melt_iceberg(iceberg, n, m)  # 빙산을 녹임
        year += 1

# 함수 실행
solution()
