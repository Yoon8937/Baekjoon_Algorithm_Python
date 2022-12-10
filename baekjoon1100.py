import sys
arr = sys.stdin.read().splitlines()
ans = 0
for i in range(len(arr)):
    if i%2==0:
        ans += [arr[i][j] for j in range(0, len(arr), 2)].count("F")
    else:
        ans += [arr[i][j] for j in range(1, len(arr), 2)].count("F")
print(ans)


### 더 나은 풀이(다른 사람)
sen = ''
for _ in range(8):
    sen += input() + '0'
print(sen[::2].count('F'))
# [ 시작 인덱스 : 끝 인덱스 : 간격 ]  #문법을 활용 못 함.
