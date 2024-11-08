import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for tree in arr:
        if tree > mid:
            sum += tree - mid

    if sum < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)