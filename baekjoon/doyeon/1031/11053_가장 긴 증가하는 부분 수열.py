T = int(input())
lst = list(map(int,input().split()))
result = []

result.append(lst[0])

for num in lst:
    # result가 비었거나, num이 result의 마지막 원소보다 크면 추가
    if not result or (num > result[-1]):
        result.append(num)
    else:
        left = 0
        right = len(result) - 1

        while left < right:
            mid = (left + right) // 2
            if result[mid] < num:
                left = mid + 1
            else:
                right = mid
        result[left] = num

print(len(result))