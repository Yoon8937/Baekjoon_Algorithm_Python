# 나의 풀이
# 1시간이 걸렸네 푸는데...
n = int(input())
for i in range(1,n*2):
    # print(" "*abs(i-n) + "*"*((n*2)-abs((n*2)-(i*2-1))) ) #첨에 푼거
    print(" "*abs(i-n) + "*"* ((n*2)-1 - abs(i-n)*2) )


# 다른 사람 풀이
for i in range(1,2*n):
    print(' '*abs(n-i)+'*'*(2*(n-abs(n-i))-1))

