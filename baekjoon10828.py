### 코드 예술이네ㄷㄷ. 공부 더 해야할듯ㅠㅠ
### 더 나은 풀이(다른사람)
import sys
stack = []
orders = sys.stdin.read().splitlines()
# print(orders) #한 번 확인해보기
print(orders)
for order in orders:
    if 'push' in order:
        stack.append(order.split()[1])
    elif 'pop' in order:
        print(stack.pop()) if stack else print(-1)
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        print(0) if stack else print(1)
    elif 'top' in order:
        print(stack[-1]) if stack else print(-1)




''''Example'''
arr = ['push 7','push 2','pop']
print('push' in arr)    #이건 False
print('push' in arr[0]) #이건 True

print(arr[0].split())   #Result => ['push', '7']
print(arr[0].split()[1])#Result => 7