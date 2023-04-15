n = int(input())
for i in range(n):
    length = int(input())
    r = input()
    a = input()

    word = []
    for j in range(length):
        if r[j] != a[j]:
            word.append(r[j])
    if len(set(word)) == 1:
        print(len(word))
    else:
        w = word.count('W')
        b = word.count('B')
        minn = min(w,b)
        exp = len(word) - (minn*2)
        print(exp + minn)




### 더 나은 풀이(다른 사람)
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    s1=input().rstrip()
    s2=input().rstrip()
    cnt1=0
    cnt2=0
    for i in range(n):
        if s1[i]!=s2[i]:
            if s1[i]=='W':
                cnt1+=1
            else:
                cnt2+=1
    print(max(cnt1,cnt2))
