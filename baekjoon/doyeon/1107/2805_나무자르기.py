import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)


def binary(trees, M, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for tree in trees:
            if tree > mid:
                # tree보다 중앙값이 더 크면
                total += tree - mid
        # 절단한 나무들의 길이가 M보다 크면 : 절단 높이를 올려본다
        if total >= M:
            result = mid
            start = mid + 1

        # 절단한 나무들의 높이가 M보다 작으면 : 절단 높이를 낮춘다
        else:
            end = mid - 1

    return result


print(binary(trees, M, start, end))
