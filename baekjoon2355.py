a,b = map(int,input().split())
x = min(a,b)
y = max(a,b)
ans = (y-x+1)*(x+y)//2
print(ans)



###계속 틀렸던 이유
# 처음에 식은 맞았으나,
# a=min(a,b), b=max(a,b) 부분에서 b가 a보다 작은 경우는 a,b에 같은 수가 할당됨.
# a,b = 1,3
a,b = 3,1
a = min(a,b)
b = max(a,b)
print('a =',a)
print('b =',b)

ans = (b-a+1)*(a+b)//2
print(ans)