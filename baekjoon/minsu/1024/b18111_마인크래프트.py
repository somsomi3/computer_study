import sys
input = sys.stdin.readline

N, M, B = map(int, input().split()) # B 인벤토리에 들고 있는 블록의 갯수
# 같은 자료를 일차원으로 받느냐 , 2차원으로 받느냐도 시간 복잡도에 차이를 일으키는 요소
flatten_matrix = [] # 평탄화한 매트릭스 == 1차원 리스트로 변경시킨 2차원 매트릭스
for y in range(N):
    land = list(map(int, input().split()))
    for i in range(M):
        flatten_matrix.append(land[i])

# range 안에 넣을 변수도 , 그때그때 계산하도록 식을 넣는 것보다 , 한 값을 정해서 넣어주는 게 좋다
min_height , max_height = min(flatten_matrix), max(flatten_matrix)

# 문제에 필요한 변수들 정리
min_time = float('inf')
optimal_height = -1 # 찾지 못했을 때 -1인가 ?

for target in range(min_height, max_height+1):
    # 블록을 더 쌓아야 할 경우 , 제거해야 할 경우 초기화 (기준 : target)
    plus = 0 # 몇 개를 쌓아야 하는지
    minus = 0 # 몇 개를 제거해야 하는지
    inventory = B # 최초 가능한 인벤토리
    for i in range(N*M): # 각 요소들 탐색
        if flatten_matrix[i] == target: continue
        elif flatten_matrix[i] - target > 0 : # target 값보다 더 클때
            minus += flatten_matrix[i] - target
        else:
            plus += target - flatten_matrix[i]
    time = plus + minus*2
    if inventory + minus < plus : continue
    if time <= min_time:
        min_time = time
        # if target > optimal_height:
        optimal_height = target

print(min_time, optimal_height)