sen = input()
arr = list(sen)
midChar = ''
midBool = False
setarr = sorted(list(set(arr)))
ans = ''
for i in range(len(setarr)):
    if arr.count(setarr[i])%2==0: #짝수일때
        ans += setarr[i] * (arr.count(setarr[i])//2)
    else: #홀수일때
        midChar += setarr[i]
        ans += setarr[i] * (arr.count(setarr[i])//2)

    if len(midChar) > 1:   #이것이 먼저 나와서 ab를 넣을때, 이 구문을 타지 못하고 for문이 종료됨. 그래서 틀렸음.
        ans = "I'm Sorry Hansoo"
        midBool = True
        break

if midBool:
    print(ans)
else:
    tmp = ans[::-1]
    ans += midChar
    ans += tmp
    print(ans)