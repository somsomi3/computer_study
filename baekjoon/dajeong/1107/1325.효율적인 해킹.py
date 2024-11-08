# https://www.acmicpc.net/problem/1325

def find(n):
    if boss[n] == n: return n
    result = find(boss[n])
    boss[n] = result
    return result

def union(t1, t2):
    a = find(t1)
    b = find(t2)
    if a == b: return
    boss[a] = b

n, m = map(int, input().split()) # n : 친구 관계, node : 노드의 개수
boss = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

print(boss)