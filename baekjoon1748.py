# 와 시불 1시간정도 이것만해서 풀었다ㅠㅠ. 한동안 못 풀줄알았는데
num = int(input())
ans = 0
for i in range(len(str(num)),0,-1):
    ans += (num-(10**(i-1))+1)*i
    num -= (num-(10**(i-1)))+1
print(ans)




# 다른 사람 풀이
n = 15
k=0
for i in range(len(n)):
    k += (int(n)-(10**i)+1)
print(k)