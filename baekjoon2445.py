n = int(input())
for i in range(1,n*2):
    print("*"*(((n*2)-abs((n*2)-2*i))//2)+ " "*abs((n*2)-2*i)  +"*"*(((n*2)-abs((n*2)-2*i))//2))


# 다른 사람 코드
# 이거 코드 잘 짰다
n = 5
for i in range(-n+1,n):
    q=abs(i)
    print('*'*(a-q)+' '*(2*q)+'*'*(a-q))