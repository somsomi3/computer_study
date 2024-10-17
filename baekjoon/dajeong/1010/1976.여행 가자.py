# https://www.acmicpc.net/problem/1976

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
for i in range(n):
    cns = list(map(int, input().split()))
    for index, c in enumerate(cns):
        if c:
            union(i+1, index+1)

nums = list(map(int, input().split()))
nb = find(nums[0])
ans = "YES"

for num in nums[1:]:
    if nb != find(num):
        ans = "NO"
        break

print(ans)