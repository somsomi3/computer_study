def find(n):
    if boss[n] == n:
        return n
    boss[n] = find(boss[n])
    return boss[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b: return
    boss[b] = a

n, m = map(int, input().split())
boss = [i for i in range(0, n+1)]
for _ in range(m):
    co, a, b = map(int, input().split())
    if co == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")