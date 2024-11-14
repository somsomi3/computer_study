def find_max_rectangle():
    global cnt
    for i in range(N):
        for j in range(N):
            # (i, j)에서 사각형 시작
            for l1 in range(1, N):  # 오른쪽 아래로 가는 길이
                for l2 in range(1, N):  # 왼쪽 아래로 가는 길이
                    path = []  # 방문한 카페 저장
                    x, y = i, j
                    valid = True

                    # 1. 오른쪽 아래
                    for _ in range(l1):
                        x, y = x + 1, y + 1
                        if 0 <= x < N and 0 <= y < N:
                            path.append(cafe[x][y])
                        else:
                            valid = False
                            break

                    # 2. 왼쪽 아래
                    for _ in range(l2):
                        x, y = x + 1, y - 1
                        if 0 <= x < N and 0 <= y < N:
                            path.append(cafe[x][y])
                        else:
                            valid = False
                            break

                    # 3. 왼쪽 위
                    for _ in range(l1):
                        x, y = x - 1, y - 1
                        if 0 <= x < N and 0 <= y < N:
                            path.append(cafe[x][y])
                        else:
                            valid = False
                            break

                    # 4. 오른쪽 위
                    for _ in range(l2):
                        x, y = x - 1, y + 1
                        if 0 <= x < N and 0 <= y < N:
                            path.append(cafe[x][y])
                        else:
                            valid = False
                            break

                    # 유효한 사각형인지 확인
                    if valid and len(path) == len(set(path)):
                        cnt = max(cnt, len(path))


# 입력 처리
T = int(input("Enter the number of test cases: "))
for t in range(1, T + 1):
    N = int(input(f"Enter the grid size for test case {t}: "))
    print(f"Enter the grid data for test case {t} (each row separated by space):")
    cafe = [list(map(int, input().split())) for _ in range(N)]

    cnt = -1  # 가능한 사각형이 없으면 -1 출력
    find_max_rectangle()
    print(f'#{t} {cnt}')
