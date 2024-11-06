import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 재귀 호출 한도를 늘려 큰 그래프에서도 DFS가 동작하도록 설정????

# 입력 처리
N, M, K = map(int, input().split())  # 격자의 크기 (N x M), 음식 개수 K 
graph = [[0] * M for _ in range(N)]  # N x M 크기의 격자를 0으로 초기화 (음식물이 없)

# 음식물 위치 표시
for _ in range(K):
    r, c = map(int, input().split())  # 음식물 위치 
    graph[r - 1][c - 1] = 1  # 입력된 위치에 음식물 표시 (1로 설정)

# 방향 설정 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # DFS에서 사용할 네 방향 (위, 아래, 왼쪽, 오른쪽)

def dfs(x, y):
    """
    DFS를 사용하여 연결된 음식물 덩어리의 크기를 계산하는 함수
    """
    stack = [(x, y)]  # 스택을 사용해 DFS 구현
    graph[x][y] = 0  # 방문한 위치는 다시 방문하지 않도록 0으로 표시
    size = 1  # 현재 음식물 덩어리의 크기를 1로 초기화

    while stack:
        cx, cy = stack.pop()  # 스택에서 현재 위치를 꺼냄
        for dx, dy in directions:  # 네 방향으로 이동
            nx, ny = cx + dx, cy + dy  # 다음 위치 계산
            # 격자 범위 내에 있고, 방문하지 않은 음식물이 있을 경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                stack.append((nx, ny))  # 스택에 다음 위치 추가
                size += 1  # 덩어리 크기 증가
    return size  # 최종 덩어리 크기 반환

# 가장 큰 음식물 덩어리 크기 찾기
max_size = 0  # 최대 음식물 덩어리 크기 초기화
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:  # 음식물이 있는 위치에서 DFS 시작
            max_size = max(max_size, dfs(i, j))  # 가장 큰 덩어리 크기 갱신

print(max_size)  # 결과 출력 (가장 큰 음식물 덩어리의 크기)
