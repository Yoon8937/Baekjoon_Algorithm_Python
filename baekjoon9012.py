## 나의 풀이
import sys
n = int(input())
ans = ''
for i in range(n):
    stack = []
    s = sys.stdin.readline().rstrip()

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack)==0:
                ans = "NO"
                break
            stack.pop()

    if len(stack)!=0 or ans == "NO":
        print("NO")
    elif len(stack)==0:
        print("YES")
    ans = ''


### 더 나은 풀이(다른 사람풀이)
# 숫자로 계산했으면 좀 더 간편했을텐데...
import sys
n = int(input())
for _ in range(n):
    str_ = sys.stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')