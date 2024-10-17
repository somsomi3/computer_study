# https://www.acmicpc.net/problem/1922

def find(n):
    if boss[n] == n:
        return n
    boss[n] = find(boss[n])
    return boss[n]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    boss[b] = a

n = int(input())
m = int(input())
boss = [i for i in range(0, n+1)]

krus = [list(map(int, input().split())) for _ in range(m)]
krus.sort(key=lambda x: x[2])
sum_v = cnt = 0

for a, b, price in krus:
    if find(a) != find(b):
        union(a, b)
        sum_v += price
        cnt += 1

        if cnt == n-1:
            break

print(sum_v)