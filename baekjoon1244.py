### 12번만에 맞추었다...문제를 끝까지 제대로 읽지않았다...그래서 출력형식이 맞지 않다고 계속 뜸.
### 계속코드를 수정하는 과정에서 조금 간결해졌다 전보다는 하지만
### 다음부터는 문제를 제대로 읽자...
import sys
length = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline().strip())

for i in range(n):
    s, num = map(int,input().split())
    if s == 1:
        for j in range(num-1,length,num):
            arr[j] = abs(arr[j]-1)
    else:
        tmpLen = min(len(arr)-num+1, num)
        idx = num - 1
        for k in range(tmpLen):
            if arr[idx-k] == arr[idx+k]:
                arr[idx-k], arr[idx+k] = abs(arr[idx-k]-1), abs(arr[idx-k]-1)
            else:
                break

for i in range(1,len(arr)+1):
    print(arr[i-1],end=" ")
    if i%20==0:
        print()