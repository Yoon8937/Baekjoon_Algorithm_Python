# 처음 나의 풀이는 너무 복잡하게 생각해서 문제를 풀어나가려 함.
# 갑자기 생각난 두 번째 풀이. 첫 번째 풀이보단 좀 간단해지긴 함.
# 그래도 이번 풀이에서는 덜 복잡하게 풀려고 생각함. 하지만 아직 뭔가 좀 아쉬운 풀이

h, w = map(int,input().split())
n = int(input())
tmp = []
for i in range(n):
    a,b = map(int,input().split())
    tmp.append([a,b])
tmp.sort()

arrw = [1 for i in range(w)]
arrh = [1 for _ in range(h)]
ww, hh = 0, 0
for i in range(n):
    if tmp[i][0] == 0:
        arrw.insert(tmp[i][1]+hh,0)
        hh += 1
    else:
        arrh.insert(tmp[i][1]+ww,0)
        ww += 1

hhh = "".join(map(str,arrh))
www = "".join(map(str,arrw))
ans1 = [len(i) for i in hhh.split("0")]
ans2 = [len(i) for i in www.split("0")]
answer = 0
for i in ans1:
    for j in ans2:
        if i*j > answer:
            answer = i*j
print(answer)



### 더 나은 풀이1(다른 사람)
width, height = map(int,input().split())
n = int(input())
w = [0,width]
h = [0, height]

for i in range(n):
    a,b = map(int,input().split())
    if a == 0:
        h.append(b)
    else:
        w.append(b)
w.sort()
h.sort()

ans = []
for i in range(1,len(h)):
    for j in range(1,len(w)):
        ans.append( (h[i]-h[i-1]) * (w[j]-w[j-1]) )
print(max(ans))


### 더 나은 풀이2(다른 사람)
width, height = map(int, input().split())
n = int(input())
w = [width]
h = [height]
for i in range(n):
    a,b = map(int,input().split())
    if a == 0:
        h.append(b)
    else:
        w.append(b)
w.sort()
h.sort()
prvh = 0
prvw = 0
answer = 0
for i in h:
    for j in w:
        tmp = (i - prvh) * (j - prvw)
        answer = max(answer, tmp)
        prvw = j
    prvh = i
    prvw = 0
print(answer)