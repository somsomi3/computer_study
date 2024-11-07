''''''

def binary_search(trees, M, start, end):
    result = 0
    while start <= end: # start가 더 커지면 종료
        mid = (end + start) // 2
        cutted = 0
        for tree in trees:
            if tree > mid:
                cutted += tree - mid #
        if cutted == M: # 운좋게 잘랐는데 딱 맞게 나왔을 때
            result = mid
            start = end
            return result
        elif cutted > M: # 자른 게 필요한 양보다 많을 때 == 괜찮긴 한데 , 높이를 더 높여서 잘라보자
            start = mid + 1
            result = mid # 괜찮긴 하니까
        else: # 아직 덜 잘랐을 때 == 높이를 더 낮춰서 잘라야 할 때
            end = mid - 1
    return result

N, M = map(int, input().split())  # N: 나무의 수 , M: 집으로 가져가고픈 나무 길이
trees = list(map(int, input().split()))

# start, end를 두고 mid 값을 확인하면서
# 전체 범위에서 절반을 먼저 본다.
start = 0
end = max(trees)
result = binary_search(trees, M, start, end)
print(result)
