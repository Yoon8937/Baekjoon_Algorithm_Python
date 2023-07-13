# 나는 무조건 정사각형이 겹치는 부분을 빼서 넓이를 구할려고 했다. 그래서 그 부분에서
# 많이 어려움을 겪었고, 어떻게 풀어야 할지 몰랐다. 블로그 힌트를 보고 알았다...

# 정사각형의 하나하나를 1로 잡는다.
# 겹치는 부분도 모두 1로 잡는다.
# 결국 2차원 리스트의 1의 갯수를 구하면 된다.

### 나의 풀이
# n = int(input())
# xy = []
# maxNum = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if max(x, y) + 10 > maxNum:
#         maxNum = max(x, y) + 10
#     xny = []
#     xny.append([y + 10, x])
#     xny.append([y + 10, x + 10])
#     xy.append(xny)
#
# arr = [[0] * maxNum for _ in range(maxNum)]
#
# for i in range(n):
#     for j in range(10):
#         for k in range(10):
#             arr[xy[i][0][0]-j-1][xy[i][0][1]+k-1] = 1
#
# cnt = 0
# for i in arr:
#     cnt += i.count(1)
# print(cnt)



###더 나은 풀이(다른 사람)
n = int(input())

arr = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int,input().split())

    for i in range(x, x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

cnt = 0
for row in arr:
    cnt += row.count(1)
print(cnt)