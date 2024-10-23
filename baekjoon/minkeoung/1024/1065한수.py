def hansu(number):
    # 주어진 숫자가 한수인지 확인하는 함수
    # 각 자릿수를 리스트로 변환
    digits = list(map(int, str(number)))
    
    # 숫자가 두 자리 이하이면 무조건 한수임
    if len(digits) <= 2:
        return True
    
    # 세 자리 이상의 숫자는 등차수열을 이루는지 확인
    return digits[1] - digits[0] == digits[2] - digits[1]

def count_hansu(N):
    # 1부터 N까지 한수의 개수를 세는 함수
    count = 0  # 한수의 개수를 세는 변수
    
    # 1부터 N까지 반복
    for i in range(1, N + 1):
        # 만약 i가 한수라면 count를 1 증가
        if hansu(i):
            count += 1
    
    # 최종적으로 한수의 개수를 반환
    return count

# 사용자 입력을 받음
N = int(input())
# N 이하의 한수 개수를 출력
print(count_hansu(N))
