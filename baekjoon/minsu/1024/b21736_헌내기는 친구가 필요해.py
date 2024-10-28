# 헌내기는 친구가 필요해
# 캠퍼스에서 이동 : 상하좌우로 이동 가능 , 방문한 곳은 used True 처리하고 ,
# 방문하지 않은 곳에서 방향배열로 접근하자 ,
# q에다가 방문할 수 있는 장소 저장하기

from collections import deque

q = deque()

N, M = map(int, input().split()) # N : 세로줄, M : 가로줄
campus = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1] # 상 하 좌 우
used = [[0] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            start = (y, x)
            q.append(start)
            used[y][x] = 1
            break

count = 0
while q:
    point = q.popleft()
    if campus[point[0]][point[1]] == 'P':
        count += 1
    for i in range(4):
        ny = point[0] + dy[i]
        nx = point[1] + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if campus[ny][nx] == 'X':
            continue
        if used[ny][nx] == 1:
            continue
        used[ny][nx] = 1
        q.append((ny, nx))

if count == 0:
    print('TT')
else :
    print(count)

