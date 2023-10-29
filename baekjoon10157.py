### 처음 푼 코드
c,r = map(int,input().split())
k = int(input())
arr = [[0]*c for _ in range(r)]
dct = 1
x,y = r,0
xx,yy=1,0
if c*r < k:
    print(0)
else:
    for i in range(k):
        if dct == 1:
            yy += 1
            x -= 1
            if x == 0 or (arr[x - 1][y] != 0):
                dct = 2
        elif dct == 2:
            xx += 1
            y += 1
            if y==c-1 or (arr[x][y+1]!=0):
                dct = 3
        elif dct == 3:
            yy -= 1
            x += 1
            if x==r-1 or (arr[x+1][y]!=0):
                dct = 4
        elif dct == 4:
            xx -= 1
            y -= 1
            if arr[x][y-1]!=0:
                dct = 1
        arr[x][y] = 1

    print(xx, yy)





###더 나은 코드(다른 사람)
def func(x, y):
    global arr
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    tmp = 1
    i = 0
    while True:
        if tmp == K:
            return x + 1, y + 1
        arr[y][x] = True

        nx = x + dx[i]
        ny = y + dy[i]
        print(nx, ny)
        if (0 <= nx < C and 0 <= ny < R):
            if arr[ny][nx] != True:
                x = nx
                y = ny
                tmp += 1
            else:
                i = (i + 1) % 4
        else:
            i = (i + 1) % 4


C, R = map(int, input().split())
K = int(input())
arr = [[False for _ in range(C + 1)] for _ in range(R + 1)]
if K > C * R:
    print(0)
else:
    print(*func(0, 0))





### 더 나은 풀이(다른 사람)
def move(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visit = [[False]*C for _ in range(R)]
    k = 0
    for i in range(1,C*R+1):
        if i == K:
           return (x+1,y+1)
        else:
            visit[y][x] = True

            print(x,y)
            x += dx[k]
            y += dy[k]
            if x<0 or y<0 or x>=C or y>=R or visit[y][x]:
                x -= dx[k]
                y -= dy[k]

                k = (k+1)%4
                x += dx[k]
                y += dy[k]


C,R = map(int,input().split())
K = int(input())

if K > C*R :
    print(0)
    exit()

print(*move(0,0))




### 다른 사람 코드 참고해서 다시 푼 코드
def method(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 0
    cnt = 0
    count = 0
    while True:
        count += 1
        arr[x][y] = True
        cnt += 1
        if cnt == k:
            print(x+1,y+1)
            print('count',count)
            break
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=c or ny<0 or ny>=r or (arr[nx][ny]==True):
            d += 1
            d = (4+d)%4
            x = x + dx[d]
            y = y + dy[d]
        else:
            x = nx
            y = ny
        # cnt += 1


c,r = map(int,input().split())
k = int(input())
arr = [[False]*r for _ in range(c)]
if c*r < k:
    print(0)
else:
    method(0,0)





### 다른 사람 코드를 좀 더 개선한 코드
def method(x,y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    arr = [[False]*r for _ in range(c)]
    d = 0

    for i in range(1,c*r+1):
        if i == k:
            return (x+1, y+1)
        else:
            arr[x][y] = True
            x += dx[d]
            y += dy[d]
            if x < 0 or x >= c or y < 0 or y >= r or (arr[x][y] == True):
                x -= dx[d]
                y -= dy[d]
                d = (d+1) % 4 ##!!!!!
                x += dx[d]
                y += dy[d]

c,r = map(int,input().split())
k = int(input())
if c*r < k:
    print(0)
else:
    print(*method(0,0))