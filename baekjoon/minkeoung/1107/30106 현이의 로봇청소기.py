from collections import deque

def count_cleanable_areas(N, M, K, heights):
    # 방향 벡터: 상, 하, 좌, 우로 이동하기 위한 방향 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    # BFS를 위한 큐 초기화, 시작 위치 (0, 0) 추가
    queue = deque([(0, 0)])
    # 시작 위치 방문 처리
    visited[0][0] = True

    cleanable_count = 1

    # 큐가 빌 때까지 BFS 실행
    while queue:
        x, y = queue.popleft()
        current_height = heights[x][y]

        # 상하좌우 방향으로 이동 가능 여부 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                next_height = heights[nx][ny]
                if abs(current_height - next_height) <= K:
                    # 방문 처리 및 큐에 추가
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    # 청소할 수 있는 영역 개수 증가
                    cleanable_count += 1

    return cleanable_count
