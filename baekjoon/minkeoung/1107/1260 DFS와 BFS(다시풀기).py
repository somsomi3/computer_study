from collections import deque

# DFS 함수 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')  # 방문한 노드 출력
    for i in sorted(graph[v]):  # 번호가 작은 것부터 방문
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')  # 방문한 노드 출력
        for i in sorted(graph[v]):  # 번호가 작은 것부터 방문
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 무방향 그래프를 만들기 위해 서로서로 그래프에 넣기
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# BFS 실행
visited = [False] * (n + 1)
bfs(graph, v, visited)