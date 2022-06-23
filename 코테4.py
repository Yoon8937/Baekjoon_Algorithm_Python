# while문으로 별찍기 2개 하기...


# #중복 된 수 제거
# arr = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
# ans = []
# for i in range(len(arr)):
#     if not arr[i] in ans:
#         ans.append(arr[i])
# print(ans)

def method(a:int,b:int)->int:
    return a if a==b else a+((a+b)//2) + b

# word = "Mississipi"
# word = "zZa"
# w = word.upper()
# print(w)
# alp = list(set(w))
# print(alp)
# amount = []
# for i in range(len(alp)):
#     cnt = 0
#     if not alp[i] in amount:
#         for j in range(len(w)):
#             if alp[i] == w[j]:
#                 cnt +=1
#         amount.append(cnt)
#     elif alp[i] in amount:
#         continue
# print(amount)
# maxx = max(amount)
# cnt = 0
# ans = ""
# for i in range(len(amount)):
#     if amount[i] >= maxx:
#         cnt +=1
#         ans += w[i]
#         if cnt>=2:
#             ans = '?'
#             break
#     else:
#         continue
# print(ans)

# word = "Mississipi"
# # word = "zZa"
# w = word.upper()
# print(w)

# 1 4 4 0 0 0 0 0 1 0
# 처음나온 알파벳만 카운트. 만약에 뒤에 같은 알파벳이 나오면 스킵(0넣기)
# word = "MISSISSIPI"
arr = list(set(word))
print(arr)
nums = [] #카운트 된 수를 저장할 리스트. 만약 전에 같은 알파벳이 나왔으면 0 넣기
lttr = [] #중복되지 않는 알파벳을 저장할 리스트.  ex) M,I,S,P
for i in range(len(word)):
    cnt = 0
    if not word[i] in lttr: #word[i]가 lttr리스트에 없을때
        lttr.append(word[i])
        for j in range(len(word)):
        # for j in range(i,len(word)):
            if word[i] == word[j]:
                cnt +=1
        nums.append(cnt)
    else: #word[i]가 lttr리스트에 있으면 nums리스트에 그냥 0추가
        nums.append(0)
print(nums)
print(lttr)




















