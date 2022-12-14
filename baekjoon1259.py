import sys
arr = []
while True:
    ip = sys.stdin.readline().rstrip()
    if ip == "0":
        break
    arr.append(ip)

for i in range(len(arr)):

    if len(arr[i])%2==0:
        if arr[i][:len(arr[i])//2] == arr[i][len(arr[i])//2:][::-1]:
            print('yes')
        else:
            print('no')
    else:
        if arr[i][:len(arr[i])//2] == arr[i][len(arr[i])//2+1:][::-1]:
            print('yes')
        else:
            print('no')




### 더 나은 풀이
import sys
while True:
    s = sys.stdin.readline().rstrip('/n')

    if s=='0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')