# 그래도 풀어서 기분 좋네...천천히 생각해서 따라가니까 풀리네
word = "baekjoon"
wlist = []
for i in range(len(word)):
    wlist.append(ord(word[i]))
print(wlist)
alphabet = [i for i in range(97,97+26)]
print(alphabet)
for i in range(len(alphabet)):
    if alphabet[i] in wlist:
        for j in range(len(wlist)):
            if alphabet[i] == wlist[j]:
                alphabet[i] = wlist.index(wlist[j])
    else:
        alphabet[i] = -1
print(alphabet)
# for i in range(len(alphabet)):
#     print(str(alphabet[i])+" ",end="")

