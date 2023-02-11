a, b = map(int,input().split())
i = 1
arr = []
while len(arr) < b:   #여기서 false지만
    for j in range(i):#for문에서 다 돌고서 while문이 false여서 종료됨. for문 다 돌고서
        arr.append(i)
    i +=1
print(arr)
print(sum(arr[a-1:b]))




### 다른 사람 풀이
a, b = 3,7
res = 0
num = 1
k = num
for i in range(1,b+1):
    if i >= a:
        res += num
    k -=1
    if k == 0:
        num += 1
        k = num
print(res)