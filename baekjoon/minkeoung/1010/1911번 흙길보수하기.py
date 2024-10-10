import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 입력 처리
n, l = map(int, input().split())  # n: 웅덩이 개수, l: 널빤지 길이
puddles = [list(map(int, input().split())) for _ in range(n)]  # 웅덩이의 시작과 끝 입력받음

# 웅덩이를 시작점 기준으로 오름차순 정렬
puddles.sort(key=lambda x: x[0])

result = 0  # 필요한 널빤지의 총 개수를 저장할 변수
boundary = 0  # 널빤지를 덮은 마지막 경계를 나타내는 변수

# 모든 웅덩이에 대해 처리
for start, end in puddles:
    # 현재 경계보다 앞쪽에 있는 웅덩이는 이미 덮여있으므로 무시
    if start > boundary:
        boundary = start  # 현재 웅덩이 시작점이 경계보다 앞에 있으면 경계 재설정

    # 덮어야 할 남은 길이 계산
    remaining_length = end - boundary
    
    if remaining_length > 0:  # 남은 구간이 있으면
        # 필요한 널빤지 개수 계산 (나누어 떨어지면 그대로, 나머지가 있으면 하나 더 필요)
        count = (remaining_length + l - 1) // l
        result += count  # 널빤지 개수 더함
        # 새 경계는 널빤지로 덮은 구간 끝으로 설정
        boundary += count * l

print(result)  # 결과 출력