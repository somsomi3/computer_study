# B1325_효율적인 해킹

'''DFS'''
'''
import sys
input = sys.stdin.readline

# 함수 정의
def dfs(x, level):
    global used, max_c, result
    if level == max_c:
        result.add(path[0])
    elif level > max_c:
        max_c = level
        result = set()
        result.add(path[0])

    for y in trust[x]:
        if used[y] == 1: continue
        used[y] = 1
        path.append(y)
        dfs(y, level+1)
        used[y] = 0
        path.pop()

# 세팅
N, M = map(int, input().split()) # N : 컴퓨터 개수 / M : 관계의 개수
trust = [[] for _ in range(N+1)] # 2차원 배열 만들거야
for _ in range(M):
    a, b = map(int, input().split())
    trust[b].append(a) # a는 b를 신뢰한다 == b에서 a를 해킹할 수 있다.
# print(trust)

# 함수 돌리면서 , 가장 많이 해킹할 수 있는 경우에 , 해킹하는 경로를 출력해야 한다.
# 함수 돌릴 조건
path = [] # 해킹 경로 저장
max_c = float('-inf') # 해킹 경로 길이 비교
used = [0]*(N+1) # 방문여부 확인
result = set() # 정답 set, 중복 제거하기 위해
for i in range(1, N+1):
    used[i] = 1
    path.append(i)
    dfs(i, 1)
    used[i] = 0 # 함수 호출 끝나고 돌아왔을 때 정리
    path.pop()

print(*result)
'''

'''BFS'''
'''튜플로 level 을 받으면 dfs level 과 같은 효과를 줄 수 있겠다'''
'''요상한 걸 혼자 위상정렬로 풀고 있었다'''
''''''
from collections import deque

def bfs():
    global count
    while q:
        now_node = q.popleft()
        for j in trust[now_node]:
            if used[j] == 1:
                continue
            used[j] = 1
            count += 1
            q.append(j)

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    trust[b].append(a)
max_count = float('-inf')
result = []
for i in range(1, N+1):
    used = [0] * (N + 1)
    start = i
    q = deque()
    q.append(i)
    used[i] = 1
    count = 1
    bfs()
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)
print(*result)
''''''
'''
5 5 
3 1
2 1
5 4
2 5
2 3
-> 1, 4가 나와야 하는데 
'''