# https://www.acmicpc.net/problem/2573

import sys
input = sys.stdin.readline
from collections import deque

def bingcnt(s,e):
    q = deque()
    v[s][e] = 1
    q.append((s,e))
    while q:
        cs, ce = q.popleft()
        for di, dj in ((1,0), (-1,0), (0,-1), (0,1)):
            ns, ne = cs + di, ce + dj
            if 0 <= ns < n and 0 <= ne < m and not v[ns][ne] and arr[ns][ne]:
                v[ns][ne] = 1
                q.append((ns, ne))

def ago(arr):
    copy_arr = [row[:] for row in arr]
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                for di, dj in ((1,0), (-1,0), (0,-1), (0,1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and not arr[ni][nj]:
                        if copy_arr[i][j]:
                            copy_arr[i][j] -= 1
    return copy_arr

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
year = cnt = 0

while True:
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not v[i][j]:
                bingcnt(i,j)
                cnt += 1
    if cnt >= 2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    arr = ago(arr)
    year += 1
    cnt = 0