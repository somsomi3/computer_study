n = int(input())
card = list(map(int, input().split()))

print(sum(card) + max(card) * (n - 2))

# 인접한 수끼리 연산해야 하므로, sort를 쓸수는 없음.
# 최대값이 한번 적게 들어가야하는데,,,
# 하지만 여전히 왜,, 위와 같이 되는지 모르겟음.