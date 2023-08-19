# 엄청 빨리 풀었다...5분 정도 안에...처음 푼 실버2
n = int(input())
arr = list(map(int,input().split()))
left = n-1
ans = [0 for i in range(n)]

for i in range(n):
    # if i == 0:
    #     ans[arr[i]] = 1
    # else:
    indexOfZero = []
    for j in range(n):
        if ans[j] == 0:
            indexOfZero.append(j)
    ans[indexOfZero[arr[i]]] = i+1

print(" ".join(map(str,ans)))



### 더 나은 풀이(다른 사람)
n=int(input())
arr=list(map(int,input().split()))[::-1]
ans=[]
for i in arr:
    ans.insert(i,n)
    n -= 1
print(*ans)
