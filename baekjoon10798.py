n = 5
arr = []
mx = 0
for _ in range(n):
    word = input()
    arr.append(word)
    if len(word) > mx:
        mx = len(word)

for i in range(n):
    if len(arr[i]) < mx:
        arr[i] = arr[i] + " "*(mx-len(arr[i]))
print(arr)

sen = ""

# 이걸 1시간이 걸리면 어떡해...시발 이거 하는데 1시간....좀 아니다
for i in range(mx):
    for j in range(n):
        sen += arr[j][i]
print(sen.replace(" ",''))





### 더 나은 풀이(다른 사람)
arr = [input().split() for _ in range(5)]
ans = ""

for i in range(15):
    for j in range(5):
        if len(arr[j]) > i:
            ans += arr[j][i]
print(ans)