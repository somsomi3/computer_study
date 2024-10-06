N = int(input())
lst = list(map(int, input().split()))
# 내림차순으로 변경
lst.sort(reverse=True)

gold = 0
for _ in range(N-1):
    i = 0
    gold += lst[i] + lst[i+1]
    del lst[i+1]
print(gold)