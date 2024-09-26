''''''



'''
# M명의 조카가 있고, N개의 과자가 있을 때,
# 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라
# 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만 과자를 하나로 합칠 순 없다.
# 과자의 길이는 양의 정수여야 한다.

M, N = map(int, input().split()) # N, M <= 1,000,000 , 시간 제한 1초, -> O(N^2는 안 돼)
lst = list(map(int, input().split())).sort() 
# 합칠 수 없고, 자를 수만 있다.
if M <= N : # 조카보다 막대과자의 수가 더 많을 땐, 내림차순으로 정렬하고, M번째의 값만 출력하면 될 텐데
    lst.sort() # O(N)
    print(lst[-M])
    # 의문 1) 시간복잡도가 이게 되는 걸까 ?
    # 의문 2) 그렇지만 긴 막대를 잘라서 줄 수 있다면 -> 
else: # 조카 수보다 막대과자의 수가 더 적을 땐. ->
'''

'''
# 과자 나눠주기
# 모든 조카에게 같은 길이의 막대 과자를 나눠줘야 한다.
# M명의 조카, N개의 과자 , 조카에게 줄 수 있는 막대 과자의 최대 길이
# 과자를 쪼갤 순 있지만, 과자를 합칠 순 없다.

def check(start, end):
    # 넘어가다 마지막까지 왔다면
    if start == end:
        return cookies[end] // M

    # 다음 단계로 넘길 수 있을 때
    # ex. 3 3 ; 10 19 22 (o, 11) # ex. 4 4 ; 10 20 25 33 (o, 16)
    elif cookies[start] < cookies[end]//M:
        return check(start + 1, end)

    # 다음 단계로 넘어갈 수 없을 때
    # ex. 3 3 ; 10 19 20 (x, 10) # ex. 4 3 ; 20 25 33 (x, 16) # ex. 5 2 ; 10 12 (x, 4)
    else: # 주어진 친구들 안에서 지지고 볶고 해야 할 때
        # 전체 값들을 다 더하고, 나눈 뒤
        max_length = float('-inf')
        for length in range(cookies[end]//M, cookies[end]):
            count = 0
            for j in cookies[start:]:
                count += j//length
            if count >= M:
                max_length = length
            else:
                break
        return max_length

M, N = map(int, input().split()) # M, N <= 1,000,000 
cookies = list(map(int, input().split())) # L < 1,000,000,000 
if sum(cookies) < M:
    print(0)
else:
    cookies.sort() 
    # 뒤에서 M번째 길이 보고, 제일 큰 거를 M보다 더 큰 조각으로 나눌 수 없으면 M이 최대,
    start_idx = max(N - M, 0)
    end_idx = N - 1
    # level = # 맨 마지막 값이 이만큼을 감당할 수 있다면 , start 값은 고려하지 않아도 된다
    result = check(start_idx, end_idx)
    print(result)

# dfs 처럼 level 을 두고 하려고 했다 -> 첫 번째 값과 마지막 값만 고려했을 뿐 , 그 중간값들을 고려해서 최적해를 만들어내지 못했다. -> X
# 시간 초과
''' # M, N, L 의 길이를 고려해야 한다. 시간 제한 1초, 30,000,000번의 연산에서 끝내야 한다

