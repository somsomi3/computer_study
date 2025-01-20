from collections import deque

def find_min_time(n, k):
    # 범위
    max_position = 100000
    visited = [0] * (max_position + 1)  # 방문 여부와 시간

    queue = deque([n]) #시작위치 큐에 넣기

    while queue:
        current = queue.popleft()

        if current == k:
            return visited[current]

        # 가는 위치 확인하기
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_position and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)


n, k = map(int, input().split())
print(find_min_time(n, k))