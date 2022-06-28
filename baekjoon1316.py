# arr = ['happy','new','year']      #3개
# arr = ['aba','abab','abcabc','a'] #1개
# arr = ['ab','aa','aca','ba','bb'] #4개
# arr = ['yzyzy','zyzyz']           #0개
# arr = ['z']                       #1개

# words = []
# n = int(input())
# for i in range(n):
#     word = input()
#     words.append(word)
# aba abab abcabc aa aca yzyzy zyzyz
# words = ['happy','new','year','hahhhpsdfjjjjkdd']
words = ['ab','aa','aca','ba','bb']
boolean = False
cnt = 0
for i in range(len(words)):
    if len(words[i]) == len(set(words[i])): #중복없이 모두 다른 문자일때
        print("words[i] : "+str(words[i]))
        cnt +=1
        continue

    else:
        print(words[i])
        for j in range(len(words[i])-1):
            if words[i][j] == words[i][j+1]:
                continue
            elif words[i][j] != words[i][j+1]:    #첫번재문자하고 두번째문자하고 다를때
                if words[i][j] in words[i][j+1:]: #첫번째문자가 두번째문자부터 마지막까지 있는가?
                    print(words[i][j])
                    boolean =True                 #있으면 True 그리고 break
                    break
                else:
                    continue
        print(boolean)
        if boolean !=True:
            print("if문의 word[i] : "+str(words[i]))
            cnt +=1
        boolean = False
print(cnt)



##### 처음에 생각한거
# word = 'hahhhpsdfjjjjkdd'
# word = 'pp'
# for i in range(len(word)-1):
#
#     if word[i] == word[i+1]:
#         print(i,word[i])
#         continue
#     elif word[i]!=word[i+1]:
#         if word[i] in word[i+1:]:
#             print("moyaho "+word[i])
#             continue


# for i in range(len(words)):
#     if len(words[i]) == len(set(words[i])):
#         cnt +=1
#         continue
#     else:


