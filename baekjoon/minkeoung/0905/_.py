
## 오르막수
import math

def combination(n, k):
    return math.comb(n, k)

N = int(input())

# 중복 조합의 개수는 (N + 10 - 1) C 10-1
result = combination(N + 10 - 1, 10 - 1)

# 10007로 나눈 나머지를 출력
print(result % 10007)


# 중복 조합에 대한 설명

