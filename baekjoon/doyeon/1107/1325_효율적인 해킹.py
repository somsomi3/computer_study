import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
computer = [[] for _ in range(N + 1)]
connect = []

# B가 해킹당하면 A를 해킹할 수 있다는 의미
for _ in range(M):
    A, B = map(int, input().split())
    computer[B].append(A)

# print(computer)


def bfs(i):
    d = deque([i])
    visited = [False] * (N + 1)
    visited[i] = True
    cnt = 1

    while d:
        i = d.popleft()
        for ni in computer[i]:
            if not visited[ni]:
                visited[ni] = True
                d.append(ni)
                cnt += 1
    # return 주의
    return cnt


max_cnt = 0
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        connect = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        connect.append(i)
print(*connect)