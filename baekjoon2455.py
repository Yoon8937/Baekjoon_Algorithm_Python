arr = []
for i in range(4):
    a,b = map(int,input().split())
    if len(arr)==0:
        arr.append(b)
    else:
        arr.append(arr[-1:][0]-a+b)
print(max(arr))






# 더 나은 풀이
li=[]
s = 0
for i in range(4):
    m,p = map(int,input().split())
    s = s-m+p
    li.append(s)

print(max(li))