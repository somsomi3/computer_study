# https://www.acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())

# 인접 리스트로 그래프 초기화
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(st):
    n = N + 1
    result = [float('inf')] * n
    result[st] = 0
    q = [(0, st)]

    while q:
        price, now = heapq.heappop(q)

        if result[now] < price: 
            continue

        # 현재 노드와 인접한 노드 탐색
        for next_node, nt_price in graph[now]:
            sum_price = price + nt_price
            if result[next_node] > sum_price:
                result[next_node] = sum_price
                heapq.heappush(q, (sum_price, next_node))

    return result

result = dijkstra(start)
for i in range(1, N + 1):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])
        
        
# import sys
# import heapq
# input = sys.stdin.readline

# N, M = map(int, input().split())
# start = int(input())

# dist = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     dist[a][b] = c

# def dijkstra(st):
#     n = N + 1
#     result = [float('inf')] * n
#     result[st] = 0
#     q = [(0, st)]

#     while q:
#         price, now = heapq.heappop(q)

#         if result[now] < price: continue

#         for i in range(n):
#             if dist[now][i] == 0: continue
#             nt_price = dist[now][i]
#             sum_price = price + nt_price
#             if result[i] > sum_price :
#                 result[i] = sum_price
#                 heapq.heappush(q, (sum_price, i))
#     return result

# result = dijkstra(start)
# for i in range(1, N+1):
#     if result[i] >= 0:
#         print(result[i])
#     else:
#         print('INF')
        