n = int(input())
arr = [0 for i in range(26)]
ans = ""
for i in range(n):
    s = input()
    arr[ord(s[0])-97] += 1

for i in range(len(arr)):
    if arr[i] > 4:
        ans += chr(i+97)

if ans == "":
    print("PREDAJA")
else:
    print(ans)



### 다른 사람 풀이(코드 잘 짰네요)
arr = [input()[0] for _ in range(int(input()))]
f = 1
for i in range(97, 123):
    if arr.count(chr(i)) >= 5:
        f = 0
        print(chr(i), end='')

if f:
    print('PREDAJA')