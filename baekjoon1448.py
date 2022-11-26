#쉬워서 빠르게 풀긴했네용
# 삼감형에서 가장 긴 변의 길이는 나머지 두 변의 길이의 합보다 작다.
import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
ans = 0
while True:
    if len(arr) < 3:
        ans = -1
        break
    if arr[-1:][0] < sum(arr[-3:-1]):
        ans = sum(arr[-3:])
        break
    del arr[-1:]
print(ans)




## 다른 사람 풀이
import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)

ttl = -1
for i in range(len(arr)-2):
    newarr = arr[i:i+3]
    if newarr[0] < newarr[1] + newarr[2]:
        ttl = newarr[0]+newarr[1]+newarr[2]
        break
print(sum)