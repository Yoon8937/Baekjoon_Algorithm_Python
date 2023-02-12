# 첫 번째 시도(시간초과)
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
distanceList = []
for i in arr:
    total = 0
    for j in arr:
        total += abs(i-j)
    distanceList.append(total)
idx = distanceList.index(min(distanceList))
print(arr[idx])


# 두 번째 시도(시간초과)
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
tmp = []
for i in range(len(arr)):
    a = (sum(arr[i:]) - len(arr[i:])*arr[i]) + ( (arr[i]*i) - sum(arr[:i]) )
    tmp.append(a)
print( arr[tmp.index(min(tmp))] )


# 세 번째 시도(정답)
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if len(arr)%2!=0:
    print(arr[len(arr)//2])
else:
    print(arr[len(arr)//2-1])




# 더 나은 풀이(다른사람)
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[(n-1) // 2])