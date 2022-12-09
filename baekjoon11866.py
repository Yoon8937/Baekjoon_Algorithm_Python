# 내가 짠 코드...queue자료구조를 활용하지 못 했음. 이 문제에서 queue자료구조를 어떻게 사용해야할지 몰랐음.
# 그래도 디버깅을 사용해서 맞출 수 있었음 :D
arr = [1,2,3,4,5,6,7]
cnt = 1
i = 0
ans = []
while True:
    if cnt%3==0:
        # print(arr,i,arr[i])
        ans.append(arr[i])
        del arr[i]      ### 여기에다가 브레이킹 포인트걸고서 디버깅함.
        i -= 1
        if len(arr) < 1:
            break
    i +=1
    cnt +=1
    if i >= len(arr):  #디버깅으로 여기서 =이 빠진것을 확인
        i = i - len(arr)
print(ans)

answer = "<"
for i in range(len(ans)):
    if i==len(ans)-1:
        answer += str(ans[i])+">"
    else:
        answer += str(ans[i])+", "
print(answer)



# 답 : [3, 6, 2, 7, 5, 1, 4]

### 다른 사람 풀이(코드가 예술이만...)
from collections import deque
n, num = 7, 3
queue = deque([1, 2, 3, 4, 5, 6, 7])

print('<', end='')
while queue: #여기를 True라고 하지않고 queue로 한 이유는 pop을
    # 계속하다보면 빈 배열이면 0이되서 결국 False이므로 while문 종료함.
    for i in range(num - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if queue: #여기도 마찬가지
        print(', ', end='')
print('>')




# from collections import deque
# arrLen, num = map(int,input().split())
# queue = deque([i for i in range(1,arrLen+1)])
# cnt = 1
# arr = []
# while len(queue) > 0:
#     if cnt%num==0:
#         arr.append(queue.popleft())
#     else:
#         queue.append(queue.popleft())
#     cnt +=1
# # print(arr)
#
# answer = "<"
# for i in range(len(arr)):
#     if i==len(arr)-1:
#         answer += str(arr[i]) + ">"
#     else:
#         answer += str(arr[i]) + ", "
# print(answer)