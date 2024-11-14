#  풀지 못함 ㅠㅠ 
# 문제이해 부족

from itertools import combinations as com

def food_making(arr, case):
    res = 0
    for f1, f2 in com(case,2):
        res += arr[f1][f2] + arr[f2][f1]
    return res


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    res = 40000
    for case in com(range(n), n//2):
        another = list(set(range(n)) - set(case))
        res1 = food_making(arr, case)
        res2 = food_making(arr, another)
        if res > abs(res1-res2):
            res = abs(res1-res2)

    print(f'#{tc} {res}')