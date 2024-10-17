# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
max_num, min_num = float('-inf'), float('inf')
arr = []
for _ in range(n):
    nums = list(map(int, input().split()))
    max_num = max(max_num, max(nums))
    min_num = min(min_num, min(nums))
    for num in nums:
        arr.append(num)

ans = [float('inf'), 0]
for tar in range(min_num, max_num+1):
    inven = b
    block = 0
    second = 0
    for i in range(len(arr)):
        if arr[i] == tar:
            continue
        elif arr[i] < tar:
            block += tar-arr[i]
            second += tar-arr[i]
        elif arr[i] > tar:
            second += (arr[i]-tar)*2
            inven += arr[i]-tar
    if block <= inven and second <= ans[0]:
        ans = [second, tar]

print(*ans)