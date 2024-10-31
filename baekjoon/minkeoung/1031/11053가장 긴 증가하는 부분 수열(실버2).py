n = int(input())
arr = list(map(int, input().split()))

# i가 0일 때 최댓값은 1
d = [1] * n

for i in range(1, n): 
    for j in range(i):  # i보다 작은 j 
        if arr[j] < arr[i]: 
            d[i] = max(d[i], d[j] + 1) 

print(max(d))