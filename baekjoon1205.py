# 첫 번째 나의 풀이
n, score, p = map(int, input().split())
if n:
    arr = list(map(int,input().split()))

    if arr[-1:][0] < score or n+1 <= p:
        arr.append(score)
        arr.sort(reverse=True)
        arr = arr[:p]
    else:
        print(-1)
        exit(0)
else:
    arr = [score]

arr.append(-1)
cnt = 1
for i in range(len(arr)-1):
    # print(cnt)
    if arr[i] == score:
        print(cnt)
        break
    if arr[i] > arr[i+1]:
        cnt = (i+1)+1





### 다른 사람 코드를 참고하고 다시 푼 코드(더 나은 풀이)
n, score, p = map(int, input().split())
if n:
    arr = list(map(int, input().split()))
    if (n < p) or (n == p and arr[-1:][0] < score):
        arr.append(score)
        arr.sort(reverse=True)
        arr = arr[:p]
        print(arr.index(score) + 1)
    else:
        print(-1)
        exit(0)
else:
    print(1)



"""
n이 0일 경우, 어떤한 숫자든 첫 번째가 된다.

등수를 잘보면 1 2 2 2 5 5 6 6 6 10인 경우, 등수가 해당 숫자의 인덱스+1인 것을 알 수 있다.
"""