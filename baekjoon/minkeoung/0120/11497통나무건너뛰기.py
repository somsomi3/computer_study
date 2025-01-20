T = int(input())

for i in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    #정렬
    level = 0

    #두칸마다 비교
    for j in range(n-2):
        level = max(level, abs(L[j]-L[j+2]))

    print(level)