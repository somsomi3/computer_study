import sys
input = sys.stdin.readline

# 입력: 단어의 개수 n을 입력받음
n = int(input())

# cnt는 그룹 단어의 개수를 세기 위한 변수, 처음에는 입력받은 단어의 개수만큼으로 설정
cnt = n

# 입력된 단어를 하나씩 검사하기 위해 n번 반복
for _ in range(n):
    word = input().strip()  # 입력받은 단어에서 공백 제거
    visited = [False] * 26  # 알파벳의 등장 여부를 기록할 리스트 (총 26개의 영어 알파벳)
    prev = ''  # 이전 문자를 저장할 변수 (prev_char에서 prev로 변경)
    group = True  # 그룹 단어인지 여부를 확인하는 변수 (is_group_word에서 group으로 변경)

    # 단어의 각 문자를 순서대로 확인
    for char in word:
        char_index = ord(char) - ord('a')  # 'a'를 0으로, 'z'를 25로 변환
        
        # 연속된 문자가 아닐 때만 처리
        if char != prev:
            # 이미 등장한 문자라면 그룹 단어가 아님
            if visited[char_index]:
                group = False
                break
            visited[char_index] = True  # 등장한 문자 기록
        prev = char  # 이전 문자를 현재 문자로 갱신

    if not group:
        cnt -= 1  # 그룹 단어가 아니므로 카운트에서 제외

# 결과 출력: 그룹 단어의 개수를 출력
print(cnt)
