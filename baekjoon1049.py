import sys
n, m = map(int,input().split())
bundle, indiv = [], []
for i in range(m):
    bun, ind = map(int,sys.stdin.readline().split())
    bundle.append(bun)
    indiv.append(ind)
bmin, imin = min(bundle), min(indiv)


cost = 0
while n > 0:
    if n < 6:
        if bmin < imin*n:
            cost += bmin
        else:
            cost += imin*n
        # break
        n -= n
    else:
        if bmin < imin*6:
            cost += bmin
        else:
            cost += imin*6
        n -= 6
print(cost)


#####다른 사람의 풀이
answer = 0
if bmin <= imin*6:
    answer = bmin*(n//6) + imin*(n%6)
    if bmin < imin*(n%6):
        answer = bmin * (n//6+1)
else:
    answer = imin * n
print(answer)
