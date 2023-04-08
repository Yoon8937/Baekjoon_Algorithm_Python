### 나의 풀이
# 제일 큰 수하고 어떤수를 합하든 간에 어차페 결과는 같다. 이것을 놓침. 그래서 계속 시간초과가 뜸.
# 힌트 받음...큰 수하고 어떤수를 하던간에 결과는 같다.
n = 5
arr = [3, 2 ,10 ,9 ,6]
mx = max(arr)
arr.remove(mx)
ans = 0
for i in range(n-1):
    mx = mx+(arr[i]/2)
print(mx)



### 다른 사람 풀이
n = int(input())
arr = list(map(int,input().split()))
ans = sum(arr) - ((sum(arr) - max(arr)) / 2)
print(ans)

