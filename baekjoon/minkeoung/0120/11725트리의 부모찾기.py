import sys
from collections import deque

input = sys.stdin.readline

# 입력
n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# BFS로 부모 노드 찾기
queue = deque([1])
parent[1] = -1  # 루트 노드 표시

while queue:
    node = queue.popleft()
    for child in tree[node]:
        if parent[child] == 0:  # 방문하지 않은 노드만
            parent[child] = node
            queue.append(child)

# 결과 출력
print('\n'.join(map(str, parent[2:])))
