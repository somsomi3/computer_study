import sys
input = sys.stdin.readline

n, m = map(int, input().split())
deudDo = set()
boDo = set()

for _ in range(n):
    deudDo.add(input().strip())

for _ in range(m):
    boDo.add(input().strip())

result = sorted(deudDo & boDo)
print(len(result))
print(*result, sep="\n")