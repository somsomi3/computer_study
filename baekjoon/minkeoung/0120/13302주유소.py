# 입력
n = int(input())  # 도시의 개수
roads = list(map(int, input().split()))  # 도로의 길이
prices = list(map(int, input().split()))  # 주유소의 리터당 가격

# 최소 비용 계산
min_price = prices[0]  # 현재까지의 최저 주유 가격
total_cost = 0  # 총 비용

for i in range(n - 1):  # 마지막 도시는 주유할 필요 없음
    # 현재까지의 최저 가격으로 이동 비용 계산
    total_cost += min_price * roads[i]
    # 다음 도시의 주유소 가격이 더 싸면 업데이트
    if prices[i + 1] < min_price:
        min_price = prices[i + 1]

# 결과 출력
print(total_cost)