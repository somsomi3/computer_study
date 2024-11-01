import sys
input =sys.stdin.readline
num = int(input())
rect = [0, 1, 3] + ([0]*998)
for i in range(3,1001):
    rect[i] = rect[i-1] + (rect[i-2]*2)
print(rect[num] % 10007)
