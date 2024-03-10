aa, bb = map(int,input().split())
a = input()
b = input()
n = int(input())
arr = list(a)[::-1]
arr.extend(list(b))
tmp = [True for _ in range(aa)]
tmp.extend([False for _ in range(bb)])
for j in range(n):
    idxs = [k for k in range(len(tmp)) if tmp[k]==True]
    tmparr = 0
    tmptf = False
    for i in idxs:
        if i == len(tmp)-1:
            break
        if tmp[i+1] == False:
            tmparr = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmparr

            tmptf = tmp[i]
            tmp[i] = tmp[i+1]
            tmp[i+1] = tmptf
print("".join(arr))



### 더 나은 풀이(다른 사람)
a, b = map(int, input().split())
li1 = list(input())
li2 = list(input())
T = int(input())
li1.reverse()
total = li1 + li2

for i in range(T):
    for j in range(len(total)-1):
        print(j,total[j])
        if total[j] in li1 and total[j+1] in li2:
            print(i, total[j], total)
            total[j], total[j+1] = total[j+1], total[j]
            if total[j+1] == li1[-1]:
                break
    print(total)
    print()
print("".join(total))



### 다시 풀어 본 나의 풀이
al,bl = map(int,input().split())
a = list(input())
a.reverse()
b = list(input())
arr = []
arr.extend(a)
arr.extend(b)
print(arr)
cnt = int(input())

for i in range(cnt):
    for j in range(len(a)):
        idx = arr.index(a[j])
        if arr[idx+1] == len(arr)-1:
            continue
        else:
            if arr[idx+1] not in a:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
print(arr)