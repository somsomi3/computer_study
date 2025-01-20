from collections import deque

# 나이트의 이동 방향 (8가지)
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    l = int(input())  # 체스판의 크기 (l x l)
    start = tuple(map(int, input().split()))  # 시작 위치
    target = tuple(map(int, input().split()))  # 목표 위치

    # BFS를 이용한 최단 거리 계산
    def bfs(start, target):
        # 방문 여부와 이동 거리 기록
        visited = [[False] * l for _ in range(l)]
        queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
        visited[start[0]][start[1]] = True

        while queue:
            x, y, cnt = queue.popleft()

            # 목표 위치에 도달한 경우
            if (x, y) == target:
                return cnt

            # 나이트의 8가지 이동
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                # 체스판 안에 있고, 방문하지 않은 경우
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

        return -1  # 목표 위치에 도달할 수 없는 경우 (문제에서는 항상 도달 가능)

    # 결과 출력
    print(bfs(start, target))
