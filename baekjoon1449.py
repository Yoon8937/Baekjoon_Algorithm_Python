# 오랜만에 푸니까, 빨리 풀었네...5분 정도...
# 문제를 잘 이해하지 못 했음 몇 개월 동안...
n, l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start,end = 0,0
bucket = 0
for i in range(n):
    if arr[i] > end:
        start = arr[i] - 0.5
        end = start + l
        bucket += 1
print(bucket)



### 다른 사람 풀이
n,l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tape = 0
answer = 0
for i in arr:
    if i > tape:
        x = i + l - 1 #좌우 0.5씩 간격을 줘야하므로
        answer += 1
print('answer =',answer)