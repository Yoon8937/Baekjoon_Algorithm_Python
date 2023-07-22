### 나의 풀이
### 17분 정도 만에 풀음...물론 전에 몇 번 시도 했었지만...
arr = [ ([0] * 101) for i in range(101) ]

n = 4
for i in range(n):
    a,b,c,d = map(int,input().split())

    for j in range(b,d):
        for k in range(a,c):
            arr[j][k] = 1

ans = 0
for i in range(len(arr)):
    ans += arr[i].count(1)
print(ans)


### 더 나은 풀이(다른 사람)
### 점이 좌표가 아닌, 박스 좌표라고 생각하고 풀었음.
matrix = [list(map(int, input().split())) for i in range(4)]
print(matrix)
a = []
for i in matrix:
    for j in range(i[0],i[2]):
        for k in range(i[1],i[3]):
            a.append((j,k))
        print(a)

print(len(set(a)))


### 더 나은 풀이를 보고, 다시 풀어 본 나의 풀이
# set을 할 때는 변형 불가능한 값이여야 한다. 즉 리스트는 안됨. 튜플로 해야됨.
n = 4
xny = []
for i in range(n):
    tmp = list(map(int,input().split()))
    xny.append(tmp)
print(xny)

ans = []
for i in range(n):

    for j in range(xny[i][1], xny[i][3]):
        for k in range(xny[i][0],xny[i][2]):
            ans.append([j,k])  # !주의! [j,k]리스트로 하면 set이 안됨 ()튜플로 해야된다.
print(len(set(ans)))





### 틀린 풀이(복잡하게 풀었음)
# n = 4
# arr = []
# for i in range(100):
#     arr.append([0]*100)
#
# xy = []
# for i in range(n):
#     a,b,c,d = map(int,input().split())
#     xy.append([[a,d],[c,d],[a,b],[c,b]])
# print(xy)
# for k in range(n):
#     for i in range(xy[k][2][1], xy[k][1][1] + 1):
#         for j in range(xy[k][0][0], xy[k][1][0] + 1):
#             arr[j][i] = 1
# print(arr)
# ans = 0
# for i in range(100):
#     ans += arr[i].count(1)
# print(ans)

# n = 4
# arr = []
# for i in range(100):
#     arr.append([0] * 100)
#
# for i in range(n):
#     a,b,c,d = map(int,input().split())
#
#     for j in range(b,c):
#         for k in range(a,c):
#             arr[j][k] = 1
# print(arr)
# ans = 0
# for i in range(0,100):
#     ans += arr[i].count(1)
# print(ans)