"""
드디어 3단계 풀었다. 약 1시간(50분)에 풀었음.
distance = [2,3,1,2,3]
price = [3,5,2,1,4,6]
만약 3일때(price[0]) 5부터 4까지(마지막 수 6은 제외) 자기 자신(3)보다
작은 것이 나올 때까지(2전까지) 합을 더하기. 그리고 자신보다 작은 것(2)가
나오면 2로 변경 후, 계속 위를 반복.
"""
n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
distance.insert(0,0)
tmpNum = price[0]
ans = 0
for i in range(1,len(distance)):
    if tmpNum > price[i]:
        ans += tmpNum*distance[i]
        tmpNum = price[i]

    elif tmpNum <= price[i]:
       ans += tmpNum*distance[i]
print(ans)

### Example ###
"""
distance = [2,3,1]
price = [5,2 4,1]       Answer : 18

distance = [3,3,4]
price = [1,1,1,1]       Answer : 10 

distance = [2,3,1,2,3]
price = [3,5,2,1,4,6]   Answer : 22
"""

