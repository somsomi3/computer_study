n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
lev = arr[0]
coin = 0

for i in range(1, n):
    coin += lev + arr[i]

print(coin)