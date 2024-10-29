''''''
'''
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i], end=' ')
print()
for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')


# set 로 받으면 , 증가하든 감소하든 중복이 제거되니까 , 가장 긴 부분수열의 길이를 뽑을 수 있다
# 중복 제거된 수열의 길이가 중요한 게 아니라 , 앞에서부터 가장 긴 걸 고르는 것
N = int(input())
lst = list(map(int, input().split()))
count = 1
dptable = [1] * N
min_value = lst[N-1] # 마지막 값을 minimum으로 잡고 , 그 값보다 작으면 minimum의 dptable 값 +1
min_idx = N-1
# 그러고 앞으로 가면서 기준값보다 작으면 +1 , 보다 크면 그 이전 값이랑 비교해야 하는데
for i in range(N-2, -1, -1):
    if lst[i] < min_value: # minimum 값보다 더 작으면 , minimum 값보다 +1 더해야 해
        dptable[i] = dptable[min_idx] + 1
        min_value = lst[i]
        min_idx = i
    else: # minimum 값보다 작진 않으면 .?
    for j in range(i+1, N):
        if lst[i] < lst[j]:
            dptable[i] = dptable[j]+1


    if lst[i] < lst[i+1]:
        count += 1
        crescendo[i] = count
print(crescendo)
'''

N = int(input())
lst = list(map(int, input().split()))
count = 1
dptable = [1] * N
# min_value = lst[N-1] # 마지막 값을 minimum으로 잡고 , 그 값보다 작으면 minimum의 dptable 값 +1
# min_idx = N-1
# 그러고 앞으로 가면서 기준값보다 작으면 +1 , 보다 크면 그 이전 값이랑 비교해야 하는데
for i in range(N-2, -1, -1):
    # if lst[i] < min_value: # minimum 값보다 더 작으면 , minimum 값보다 +1 더해야 해
    #     dptable[i] = dptable[min_idx] + 1
    #     min_value = lst[i]
    #     min_idx = i
    # else: # minimum 값보다 작진 않으면 .?
    for j in range(i+1, N):
        if lst[i] < lst[j]:
            dptable[i] = max(dptable[i], dptable[j]+1)
print(max(dptable))

