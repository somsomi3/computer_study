# B30106_현이의 로봇 청소기

dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1] # 상 하 좌 우

from collections import deque

def bfs():
    global count

    while q:
        (now_y, now_x) = q.popleft()
        height = matrix[now_y][now_x] # 그 지점에서의 높이
        # 방향배열
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if used[ny][nx] != 0 :
                continue
            if abs(matrix[ny][nx] - height) > K: # 새로운 지점과 현재 지점의 높이 차이가 K 초과일 때 - 생략
                continue
            else:
                used[ny][nx] = count
                q.append((ny, nx))
    count += 1

# N * M 크기의 현이의 방 , 최대 높이차 K
# 로봇 청소기는 높이 차이가 K 이하인 영역 사이에서만 이동한다
N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
used = [[0 for _ in range(M)] for _ in range(N)]
# print(used)
count = 1
q = deque()
for y in range(N):
    for x in range(M):
        # 출발점 찾기
        if used[y][x] != 0:
            continue
        used[y][x] = count
        q.append((y, x))
        bfs()
        # count += 1
# print(used)
print(count-1)