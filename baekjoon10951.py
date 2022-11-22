import sys
arr = sys.stdin.read().splitlines()
for i in range(len(arr)):
    print(int(arr[i].split()[0]) + int(arr[i].split()[1]))



### 이러면 아무것도 입력안하고 엔터를 쳤을 때 while문이 종료(다른 사람 풀이)
while True:
    try:
        A, B= map(int,input().split())
        print(A+B)
    except:
        break