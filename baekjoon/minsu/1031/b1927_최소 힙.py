# b1927_최소힙
import heapq

min_heapq = []
N = int(input())
x_list = []
for _ in range(N):
    x = int(input())
    x_list.append(x)
result = []
for x in x_list:
    if x == 0:
        # 배열에서 가장 작은 값을 출력하고 , 그 값을 배열에서 제거
        if min_heapq:
            min_x = heapq.heappop(min_heapq)
            result.append(min_x)
        else:
            result.append(0)
    else:
        # heapq 배열에 x를 추가
        heapq.heappush(min_heapq, x)
print(*result, sep='\n')