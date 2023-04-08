n = int(input())
num = int(input())
arr = []
for i in range(n):
    arr.append([0] * n)
arr[n // 2][n // 2] = 1
x, y = n // 2, n // 2
a, b = x + 1, y + 1
for i in range(1, n * n):
    if y == 0:
        x -= 1
    elif x == (n - 1):
        y -= 1
    elif y == (n - 1):
        x += 1
    elif x == 0:
        y += 1
    elif (arr[x - 1][y] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0 and arr[x][y - 1] == 0) or (
            arr[x][y + 1] != 0 and arr[x - 1][y] == 0):
        x -= 1
    elif arr[x][y - 1] == 0 and arr[x - 1][y] != 0:  # go left
        y -= 1
    elif arr[x + 1][y] == 0 and arr[x][y - 1] != 0:  # down
        x += 1
    elif arr[x + 1][y] != 0 and arr[x][y + 1] == 0:  # go right
        y += 1
    arr[x][y] = i + 1
    if arr[x][y] == num:
        a, b = x + 1, y + 1

for i in range(len(arr)):
    print(" ".join(list(map(str, arr[i]))))
print(a, b)


### 더 나은 풀이(다른사람)
N = int(input())
target = int(input())

arr = [[0] * N for _ in range(N)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

ans = []
x, y = 0, -1
d = 0
for i in range(N**2, 0, -1):
    nx, ny = x + dxs[d], y + dys[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[ny][nx] != 0:
        d += 1
        d %= 4

        nx, ny = x + dxs[d], y + dys[d]

    arr[ny][nx] = i
    x, y = nx, ny
    if i == target:
        ans =[y+1,x+1]

for i in arr:
    print(" ".join(map(str,i)))
print(" ".join(map(str,ans)))













