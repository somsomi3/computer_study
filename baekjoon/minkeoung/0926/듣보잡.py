import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = dict()
answer = []
for i in range(n):
    x = input()
    if x not in arr1: #문자열이 arr1에 없을 때만 딕셔너리에 추가.중복 피하기 
        arr1[x] = i

for i in range(m):
    y = input()
    if y in arr1: # 만약 arr1에 존재하면 그 문자열을 answer 리스트에 추가
        answer.append(y)
        
answer.sort()
print(len(answer)) # 공통으로 존재하는 문자열의 개수를 출력
print(''.join(answer), end = '')