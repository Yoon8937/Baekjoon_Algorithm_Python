n, box = map(int,input().split())
if n == 0:
    print(0)
else:
    arr = list(map(int,input().split()))
    const = box
    answer = 0
    for i in range(n):
        if arr[i] > box:
            box = const
            box -= arr[i]
            answer += 1
        else:
            if const == box:
                answer += 1
            box -= arr[i]
    print(answer)



### 더 나은 풀이(다른 사람)
N, M = map(int, input().split())
cnt = 0
if N:
    book_list = list(map(int, input().split()))
    now = 0
    for book in book_list:
        if now + book <= M:
            now += book
        else:
            cnt += 1
            now = book
    cnt += 1
print(cnt)



### 더 나은 풀이(다른 사람)
N, M = map(int, input().split(' '))
books = []
if N != 0:
    books = list(map(int, input().split(' ')))

k, cnt = 0, 0
for book in books:
    if cnt == 0:
        cnt += 1
    if k + book > M:
        k = book
        cnt += 1
    else:
        k += book
print(cnt)



