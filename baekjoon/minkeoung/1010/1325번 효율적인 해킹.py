import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
n, m = map(int, input().split())  
graph = [[] for _ in range(n + 1)]  


for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # b가 해킹되면 a도 해킹 가능하므로 b에서 a로 연결

# BFS 함수: 시작 노드 v에서부터 탐색하여 연결된 노드의 개수를 반환
def bfs(v):
    queue = deque([v])  # 시작 노드를 큐에 넣음
    cnt = 1  # 해킹 가능한 컴퓨터 수 (자기 자신 포함)
    visited = [False] * (n + 1)  
    visited[v] = True  # 시작 노드를 방문했다고 표시

    while queue:  # 큐가 빌 때까지 반복
        x = queue.popleft()  # 큐에서 하나의 노드를 꺼냄
        for i in graph[x]:  # 해당 노드와 연결된 모든 노드들을 탐색
            if not visited[i]:  # 방문하지 않은 노드라면
                visited[i] = True  # 방문했다고 표시
                queue.append(i)  # 큐에 해당 노드를 추가
                cnt += 1  # 해킹 가능한 컴퓨터 수 증가

    return cnt  # 최종적으로 해킹 가능한 컴퓨터 수 반환

# 결과를 저장할 리스트
result = []
for i in range(1, n + 1):  # 각 컴퓨터를 시작점으로 BFS를 실행
    result.append(bfs(i))  # 각 컴퓨터에서 해킹할 수 있는 컴퓨터 수를 저장


max_hack = max(result)  # 해킹할 수 있는 컴퓨터의 최대 수


for i in range(len(result)):
    if max_hack == result[i]:
        print(i + 1, end=' ')  # 1번 컴퓨터부터 출력해야 하므로 인덱스에 1을 더함