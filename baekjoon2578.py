arr = []
lst = []
for i in range(10):
    tmp = list(map(int,input().split()))
    if i < 5:
        arr.extend(tmp)
    else:
        lst.extend(tmp)
cnt = 0
tmp = []
i = 0
# while len(tmp) != 3: #이것 때문에 틀림
while len(tmp) < 3:
    idx = arr.index(lst[i])
    arr[idx] = 0

    if sum(arr[idx//5*5: idx//5*5+5]) == 0:
        if list(range(idx//5*5, idx//5*5+5)) not in tmp:
            tmp.append(list(range(idx//5*5, idx//5*5+5)))
            cnt += 1
    if sum(list(arr[k] for k in range(idx%5,len(arr),5))) == 0:
        if list(range(idx%5,len(arr),5)) not in tmp:
            tmp.append(list(range(idx%5,len(arr),5)))
            cnt += 1
    if idx in list(range(4,21 ,4)) and sum(list(arr[l] for l in range(4,21 ,4)))==0:
        if list(range(4,21 ,4)) not in tmp:
            tmp.append(list(range(4,21 ,4)))
            cnt += 1
    if idx in list(range(0,len(arr),6)) and sum([arr[i] for i in range(0,len(arr),6)])==0:
        if list(range(0,len(arr),6)) not in tmp:
            tmp.append(list(range(0,len(arr),6)))
            cnt += 1
    i += 1
print(i)

# 아래의 경우, 즉 동시에 2,3개가 빙고가 될 때를 고려하지 않음(len(tmp) !=3).
# 하지만 len(tmp) < 3인 경우로 하여, 3보다 커지면 break해야 됨.
# 9 10 1 11 12
# 13 14 2 15 16
# 3 4 17 5 6
# 18 19 7 20 21
# 22 23 8 24 25
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25



### 더 나은 풀이(다른 사람)
board = [list(map(int, input().split())) for _ in range(5)]
ch = [0] * 12
hashmap = {board[r][c] : (r, c) for r in range(5) for c in range(5)}

res = 0
tmp = False
for _ in range(5):
    num_list = list(map(int, input().split()))
    if tmp:
        break
    for num in num_list:
        res += 1
        ch[hashmap[num][0]] += 1
        ch[hashmap[num][1] + 5] += 1
        if hashmap[num][0] ==hashmap[num][1]:
            ch[-2] += 1

        if sum(hashmap[num]) == 4:
            ch[-1] += 1

        if ch.count(5) >= 3:
            print(res)
            tmp = True
            break