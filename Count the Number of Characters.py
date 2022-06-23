#######문자 갯수 세기#######
### F -> 4개, f-> 1개, G->3개... 처음에 푼거
asdf = ['F','f','F','F','F','A','G','G','R','G','Q','B','Q','B','B','D','D','P','Z','P','P','Z']
dicc = {}
for i in range(len(asdf)):
    cnt = 0
    for j in range(len(asdf)):
        if not asdf[i] in dicc.values():
            if asdf[i] == asdf[j]:
                cnt +=1
                dicc[asdf[i]] = cnt
            elif asdf[i] in dicc.values():
                continue
print(dicc)


# arr = [1,2,2,3,3,3,4,4,4,7,7,7,7,7] #->  1 :1개, 2:2개, 3:3개 ...
arr = ['a','b','b','c','c','c','f','f','f','f']
dic = {}
for i in range(len(arr)):
    cnt = 0
    if not arr[i] in dic.keys():
        for j in range(i,len(arr)):
            if arr[i] == arr[j]:
                cnt +=1
        dic[arr[i]] = cnt
    elif arr[i] in dic.keys():
        continue
print(dic)


arrr = ['F','f','F','F','F','A','G','G','R','G','Q','B','Q','B','B','D','D','P','Z','P','P','Z']
dictt = {}
for i in range(len(arrr)):
    if not arrr[i] in dictt.keys():
        dictt[arrr[i]] = 1
    elif arrr[i] in dictt.keys():
        dictt[arrr[i]] +=1
print(dictt)


s = "MISSISSIPI"
ndict = {}
for i in range(len(s)):
    cnt = 0
    for j in range(i,len(s)):
        if s[i] == s[j]:
            cnt +=1

    if not s[i] in ndict.keys():
        ndict[s[i]] = cnt
print(ndict)


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










