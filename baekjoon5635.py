n = int(input())
dic = {}
for i in range(n):
    name,d,m,y = map(str,input().split())
    if len(m) ==1:
        m += "0"
    if len(d) ==1:
        d += "0"
    dic[y+m[::-1]+d[::-1]] = name
arr = sorted(dic.items())

print(arr[-1::][0][1])
print(arr[1][1])




### 더 나은 풀이(다른 사람)
import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    n,d,m,y = input().rstrip().split()
    d,m,y = map(int,(d,m,y))
    lst.append((y,m,d,n))
lst.sort()
print(lst)
print(lst[-1][3])
print(lst[0][3])
