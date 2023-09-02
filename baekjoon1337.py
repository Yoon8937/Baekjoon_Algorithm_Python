import sys
n = int(input())
arr = list(map(int,sys.stdin.read().splitlines()))
arr.sort()
ans = []
def method(tmp:list,start:int,end:int)->int:
    cnt = 0
    for i in tmp:
        if start<=i<=end:
            cnt +=1
        else:
            break
    return cnt

for i in range(n):
    tmp = arr[arr.index(arr[i]):]
    num = method(tmp,arr[i],arr[i]+4)
    ans.append(num)
print(5-max(ans))




### 더 나은 풀이(다른 사람)
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort
ans = 4
for i in li :
    cnt = 0
    for j in range(1,5) :
        if i-j not in li :
            cnt+=1
    ans = min(ans,cnt)
print(ans)


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
ans = 4
for i in arr:
    tmp = 4
    for j in range(1,5):
        if i+j in arr:
           tmp -= 1
    ans = min(ans, tmp)
print(ans)