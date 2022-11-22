import sys
n = int(input())
for i in range(n):
    qnty, idx = map(int,input().split())
    queue = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    while True:
        if queue[0]==max(queue):#가장 큰 수가 첫번째에 왔을때 삭제
            cnt += 1
            if queue.index(queue[0]) == idx:#인덱스끼리 비교. 숫자끼리 비교하면 안됨!조심!
                print(cnt)
                break
            queue.pop(0)
        else:
            queue.append(queue.pop(0))
        idx -=1     #제일 큰 수가 제거되거나, 땡겨지므로 idx에 -1을한다.
        if idx < 0: #BUT 인덱스가 0일때 마이너스면 맨 뒤로 보내주기.
            idx = len(queue)-1


# 약 50분 안에 풀었네..