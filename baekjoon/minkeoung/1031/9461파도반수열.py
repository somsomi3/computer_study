import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력
t = int(input())

# 파도반 수열을 저장할 배열 초기화 (100까지 미리 계산)
arr = [0] * 101
arr[1] = arr[2] = arr[3] = 1

# 점화식에 따라 arr 배열 미리 계산
for i in range(4, 101):
    arr[i] = arr[i - 2] + arr[i - 3]

# 각 테스트 케이스마다 결과 출력
for _ in range(t):
    n = int(input())
    print(arr[n])