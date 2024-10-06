import sys
input = sys.stdin.read

# 모든 입력을 한 번에 읽고, 공백으로 분리
data = input().split()

# 첫 두 개는 N과 M
N, M = map(int, data[:2])

# 그 이후로는 N + M 개의 문자열
lst = data[2:]

# N과 M을 기반으로 리스트 분할
N_lst = set()  # 집합으로 변경
M_lst = set()  # 집합으로 변경

# N과 M 중 작은 값만큼 각각 리스트로 분리
for _ in range(min(N, M)):
    N_lst.add(lst.pop(0))
    M_lst.add(lst.pop())

# N과 M이 다른 경우, 남은 요소를 각각 처리
for _ in range(abs(N - M)):
    if N > M:
        N_lst.add(lst.pop())
    else:
        M_lst.add(lst.pop())

# N_lst와 M_lst에서 중복된 항목 찾기
same = sorted(N_lst & M_lst)  # 교집합을 이용해 중복된 항목 찾기

# 결과 출력
print(len(same))
print(*same, sep='\n')