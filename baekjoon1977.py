m = int(input())
n = int(input())
arr = [i for i in range(int(m**(1/2)),int(n**(1/2))+1)]
if arr[0]**2 < m:
    del arr[0]
if len(arr) == 0:
    print(-1)
else:
    tmp = [i*i for i in arr]
    print(sum(tmp));print(tmp[0])




### 다른 사람 풀이
m = int(input())
n = int(input())
num = []
i = 1
while i**2<=n:
    if m<= i**2<=n:
        num.append(i ** 2)
    i +=1
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])