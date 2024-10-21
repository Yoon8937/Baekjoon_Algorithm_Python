"""
이렇게 쉬운건데 왜 이렇게 어려워하고 계속 틀렸는지 모르겠다...
아마 내가 하나의 좌표를 기준으로 동서남북의 개수를 세는 것을 생각 못 했다나보다...아마 착각한 것 같다.
아니면 if '0' in tmp and arr[i][j] == '1': 이 부분에서 아마 arr[i][j] == '1' 이 조건을 빼먹은 듯..

문제를 너무 어렵게 생각하는 경향이 있는 것 같음.
"""
n = int(input())
arr = [['0']*101 for _ in range(101)]
for i in range(n):
    x, y = map(int,input().split())
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k] = '1'

totalCnt = 0
for i in range(1, 100):
    if '1' in arr[i]:
        for j in range(1, 100):
            tmp = [arr[i][j+1], arr[i+1][j], arr[i][j-1], arr[i-1][j]]
            if '0' in tmp and arr[i][j] == '1':
                totalCnt += tmp.count('0')

print(totalCnt)




###더 나은 풀이(다른 사람)
import sys
input = sys.stdin.readline
N = int(input().strip())
big_rec = [[0] * 102 for _ in range(102)]
for _ in range(N):
    r, c = map(int, input().split())
    for i in range(r+1, r + 11):
        for j in range(c+1, c+11):
            big_rec[i][j] = 1

ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if big_rec[i][j]:
            ans += 4 - (big_rec[i-1][j] + big_rec[i][j-1] + big_rec[i+1][j] + big_rec[i][j+1])
print(ans)