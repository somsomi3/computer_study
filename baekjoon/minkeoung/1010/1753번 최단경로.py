import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 입력
V, E = map(int, input().split())
K = int(input())

# 그래프 초기화
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 노드면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            # 더 짧은 경로를 발견하면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(K)

# 결과 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
