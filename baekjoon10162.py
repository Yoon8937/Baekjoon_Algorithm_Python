num = 100
arr = [300,60,10]
ans = []

for i in arr:
    if i==10 and num%i!=0:
        ans = []
        ans.append(-1)
        break
    ans.append(num//i)
    num %= i

for i in ans:
    print(i,end=" ")



###더 나은 풀이
T = int(input())

if T%10:
    print(-1)
else:
    print(f'{T//300} {T%300//60} {T%300%60//10}')