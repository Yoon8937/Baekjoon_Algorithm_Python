# 이거 푸는데 거의 두 달이 걸렸네;;

# 메모리 초과됨.
#처음에 풀었던 방식(벌집이 만들어지는 것을 리스트에다가 넣음)
n = 21
arr = []
cnt = 6
p = 0
a = []
for i in range(1,n+1):
    if i==1:
        a.append(1)
        arr.append(a)
        p = i + cnt
        a = []
        continue
    elif i <= p:
        a.append(i)
        if i==n or i==p:
            arr.append(a)
            cnt +=6
            p +=cnt
            a = []
print(arr)
print(len(arr))


# 시간초과
# 두 번째 풀었던 방식
n = 23
cnt = 0
limit = 2
for i in range(1,n+1):
    if i==1:
        cnt +=1
    if limit==i:
        cnt +=1
        limit += (6 * (cnt-1))
print(cnt)



# 세 번째 풀었던 방식(계차수열을 이용함)
n = 19
cnt = 0
lim = 1
for i in range(1,n+1):
    if i==lim:
        lim = 2 + ( (6*cnt*(cnt+1))//2 )
        cnt += 1
print(cnt)


# 세 번째 풀이를 이용함
n = 18
cnt = 0
while True:
    if n < 2 + ( (6*cnt*(cnt+1))//2 ):
        cnt +=1
        break
    cnt +=1
print(cnt)
