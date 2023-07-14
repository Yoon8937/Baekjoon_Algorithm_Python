import sys
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
mx = arr[-1]
if mx >= sum(arr[:-1]):
    print(sum(arr[:-1]) + sum(arr[:-1])-1)
else:
    print(sum(arr))



### 더 나은 풀이(다른 사람)
arr = list(map(int,input().split()))
arr.sort()
print(sum(arr)-arr[2] + min(arr[2], arr[0]+arr[1]-1))
