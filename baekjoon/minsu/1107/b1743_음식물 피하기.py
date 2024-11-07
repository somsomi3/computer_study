
from collections import deque

# 상하좌우로 가장 큰 것들
# BFS로 뽑는데 , 한 묶음의 수 정하기

# 상하좌우 방향
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global count

    while q:
        (now_y, now_x) = q.popleft()

        for i in range(4): # 상하좌우 4방향
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if matrix[ny][nx] == 1: # 만약 쓰레기가 존재한다면
                if used[ny][nx] != 0: # 이미 방문했던 노드라면
                    continue
                count += 1
                used[ny][nx] = 1
                q.append((ny, nx))

N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
used = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

q = deque()
max_count = float('-inf')
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0:
            continue
        if used[y][x] != 0:
            continue
        # 쓰레기가 있고 , 방문한 적 없는 노드라면
        count = 1 # 쓰레기 개수 초기화
        used[y][x] = 1 # 방문할 거다
        q.append((y, x)) # deque에 start 지점 추가
        bfs()
        if count > max_count:
            max_count = count
print(max_count)


