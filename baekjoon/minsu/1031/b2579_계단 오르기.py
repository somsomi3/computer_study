N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
dptable = [[0, 0] for _ in range(N)]
result = [0] * N
dptable[0] = [0, lst[0]]
result[0] = lst[0]
if N > 1:
    dptable[1] = [lst[1], lst[0]+lst[1]]
    result[1] = lst[0]+lst[1]
if N > 2 :
    for i in range(2, N):
        # x = i % 2
        dptable[i][0] = max(dptable[i-2]) + lst[i]
        dptable[i][1] = dptable[i-1][0] + lst[i]
    for i in range(2, N):
        result[i] = max(result[i-2] + lst[i], max(dptable[i]))
print(result[N-1])