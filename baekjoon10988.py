# 첫 번재 풀이
# for i in range(len(w)//2-1):
#     if w[i] == w[len(w)-1-i]:
#         ans = 1
#     else:
#         ans = 0
#         break
w = input()
ans = 1
for i in range(len(w)//2):
    if w[i] != w[len(w)-1-i]:
        ans = 0
        break
print(ans)






# 더 나은 풀이(다른사람)
lp =list(str(input()))

if list(reversed(alp)) == alp:
    print(1)
else:
    print(0)