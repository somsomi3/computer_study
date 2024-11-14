# 방향
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]


# dfs 함수
def dfs(i, j, length, remaining_k):
    global result
    visited[i][j] = 1  # 방문 표시
    result = max(result, length)  # 최댓값 갱신

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if mountain[ni][nj] < mountain[i][j]:  # 다음 위치가 더 낮은 경우
                dfs(ni, nj, length + 1, remaining_k)
            elif remaining_k > 0 and mountain[ni][nj] - K < mountain[i][j]:  # 깎아서 이동 가능한 경우
                original_height = mountain[ni][nj]
                mountain[ni][nj] = mountain[i][j] - 1  # 깎아서 이동
                dfs(ni, nj, length + 1, 0)
                mountain[ni][nj] = original_height  # 원상복구

    visited[i][j] = 0  # 방문 해제


# 입력
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            top = max(top, mountain[i][j])  # 최고점 찾기

    visited = [[0] * N for _ in range(N)]  # 방문 배열 초기화
    result = 0  # 결과 초기화

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:  # 최고점에서 DFS 시작
                dfs(i, j, 1, K)

    print(f"#{tc} {result}")
