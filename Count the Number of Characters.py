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


