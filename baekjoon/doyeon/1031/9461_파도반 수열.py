T = int(input())
triangle = [0,1,1,1] + ([0]*97)
# print(triangle)

for i in range(4,101):
    # append: 맨 뒤에 요소를 추가하기 때문에 사용 불가능
    triangle[i] = (triangle[i-2]+triangle[i-3])

for _ in range(T):
    N = int(input())
    print(triangle[N])