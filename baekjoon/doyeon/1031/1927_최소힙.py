# import sys,heapq
# input = sys.stdin.readline
#
# T = int(input())
# lst = []
# stack = []
# result = []
#
# for _ in range(T):
#     lst.append(int(input()))
#
# for el in lst:
#     if el == 0:
#         if stack:
#             result.sort()
#             result.append(stack.pop(0))
#         else:
#             result.append(0)
#     else:
#         stack.append(el)
#
# print(*result,sep='\n')
'''
일단 위의 코드는 틀리기도했는데 자료구조가 heapq 즉 priority queue를 사용하지 않아서 시간복잡도가 O(n)으로 문제에서 요구하는 O(logN)이 아니다.
그래서 heapq로 해야한다.
'''


import heapq,sys
input = sys.stdin.readline

T = int(input())
lst = []
cnt = 0
for _ in range(T):
    i = int(input())
    if i == 0:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)

    else:
        heapq.heappush(lst, i)
