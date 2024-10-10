import sys
input = sys.stdin.readline

# 입력 처리
N, M, B = map(int, input().split()) 
ground = [list(map(int, input().split())) for _ in range(N)]  # 땅의 높이 정보를 2차원 리스트로 받음

# 땅의 최소 높이와 최대 높이 계산
min_height = min(map(min, ground))  # 전체 땅의 최소 높이
max_height = max(map(max, ground))  # 전체 땅의 최대 높이

# 최적 결과를 저장할 변수
optimal_time = float('inf')
optimal_height = -1

# 가능한 모든 높이(h)에 대해 탐색
for target_height in range(min_height, max_height + 1):
    remove_blocks = 0  # 블록을 제거해야 하는 수
    add_blocks = 0     # 블록을 추가해야 하는 수

    # 땅을 순회하면서 블록을 추가하거나 제거해야 하는 수 계산
    for row in ground:
        for block_height in row:
            if block_height > target_height:
                remove_blocks += block_height - target_height  # 블록을 제거
            else:
                add_blocks += target_height - block_height  # 블록을 추가

    # 인벤토리와 제거한 블록으로 추가할 블록을 충당할 수 있는지 확인
    if remove_blocks + B >= add_blocks:
        # 총 걸리는 시간 계산: 제거 작업은 2초, 추가 작업은 1초
        current_time = remove_blocks * 2 + add_blocks

        # 최적의 시간을 찾으면 갱신
        if current_time < optimal_time or (current_time == optimal_time and target_height > optimal_height):
            optimal_time = current_time
            optimal_height = target_height

# 결과 출력
print(optimal_time, optimal_height)
