##백준 if문 1번
# x,y = map(int, input().split())
# print(x,y)
# ans =""
# if x>y:
#     ans = ">"
# elif x<y:
#     ans = "<"
# else:
#     ans = "=="
# print(ans)
#
# print('>' if x>y else('<' if x<y else '=='))# 한줄로 가능

# score = int(input())
# # print('A' if 90<=score and score<=100 else('B' if 80<=score and score<=89 \
# #                                            else('C' if 70<=score and score<=79 \
# #                                                 else('D' if 60<=score and score<=69 else "F"))))
# grade = ""
# if 90<=score and score<=100:
#     print("A")
# elif 80<=score and score<=89:
#     print('B')
# elif 70<=score and score<=79:
#     print('C')
# elif 60<=score and score<=69:
#     print('D')
# else:
#     print('F')

# year = int(input())
# # if year%4==0 and (year%100!=0 or year%400==0):
# #     print(1)
# # else:
# #     print(0)
# print(1 if year%4==0 and (year%100!=0 or year%400==0) else 0)

# hour, min = map(int,input().split())
# if min<45:
#     if(hour==0):
#         hour = 24
#     hour -=1
#     min +=60
# min = min - 45
# print(hour, min)

# hour, min = map(int,input().split())
# pmin = int(input)
#
# if min + pmin>=60:


# l = int(input())
# ll = []
# for i in range(l):
#     a,b = map(int,input().split())
#     ll.append(a+b)
# for i in range(len(ll)):
#     print(ll[i])

# for i in range(l):
#     a,b=map(int,sys.stdin.readline().split())
#     print(a+b)


# n = int(sys.stdin.readline().strip())
# text = ''
# for i in range(n):
#     a,b = map(int, sys.stdin.readline().split())
#     text+=f'{a+b}\n' #이거 보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(text)

# num =int(input())
# sum =0
# for i in range(1,num+1):
#     sum +=i
# print(sum)
# n = int(input())
# print((n**2+n)//2)
#
# n = int(input())
# print((n * (n+1)) // 2)

# num = "17037300"
# list = []
#
# for i in range(10):
#     cnt = 0
#     for j in range(len(num)):
#         if i==int(num[j]): #처음에 그냥 i==num[j]로만 써서 str이여서 비교가 안됐음
#             cnt +=1
#     list.append(cnt)
# print(list)
# print(2%10)

# a = [1,2,3,4,5,5]
# b = []
# for i in range(len(a)):
#     if not b in a: #근데 b안에 있는게 똑같은게 있으면 그냥 continue
#         b.append(a[i])
# print(b)

# num = 17037300
# arr = []
# for i in range(10):
#     arr.append(0)

# while(num!=0):
#     arr[num%10] +=1
#     num //=10
# print(arr)

# x =list(str(num))
# print(x)
# for i in range(10):
#     y = x.count(str(i))
#     print(y)

# nums = int(input())
# arr = []
# for i in range(nums):
#     num = int(input())
#     arr.append(num)
# print(min(arr),max(arr))

# A = [int(input()) for _ in range(9)]  #############보기##############
# print(type(A))
# print(max(A))
# print(A.index(max(A))+1)

# n = int(input())
# arr = []
# for i in range(n):
#     a = input()
#     cnt =0
#     count=0
#     for j in range(len(a)):
#         if a[j]=='O':
#            count +=1
#         elif a[j]== 'X':
#             count =0
#         cnt +=count
#     arr.append(cnt)
#     print(arr[i])

# a = "OOXXOXXOOO"
# cnt = 0
# count = 0
# for i in range(len(a)):
#
#     if a[i] == 'O':
#         count +=1
#     elif a[i] =='X':
#         count = 0
#     print(cnt,count)
#     cnt +=count
#
# print(cnt)


# n = int(input())
# arr = []
# ans = []
# for i in range(n):
#     s = input()
#     arr.append(s)
#
# for i in range(n):
#     cnt =0
#     count =0
#     for j in range(len(arr[i])):
#         if arr[i][j] == 'O':
#             count +=1
#             cnt += count
#         elif arr[i][j] =='X':
#             count = 0
#     ans.append(cnt)
#     print(ans[i])



## %42 때의 개수
# arr = [42,84,252,420,840,126,42,84,420,126]
# arr = [39,40,41,42,43,44,82,83,84,85]
# arr = [1,2,3,4,5,6,7,8,9,10]

# arr = []
# for i in range(10):
#     n = int(input())
#     arr.append(n)
# ans = []
# for i in range(len(arr)):
#     r = arr[i] % 42
#     ans.append(r)
# print(ans)
# print(set(ans))
# print(len(set(ans)))

# arr = []
# for i in range(10):
#     n = int(input()) % 42
#     arr.append(n)
# print(len(set(arr)))


# arr =[]
# for i in range(10):
#     n = int(input())
#     arr.append(n%42)
arr = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
ans = []
for i in range(len(arr)):
    if not arr[i] in ans:
        ans.append(arr[i])
print(ans)

# arr = []
# ans = []
# for i in range(10):
#     n = int(input()) % 42
#     arr.append(n)
#
# for i in range(len(arr)):
#     if not arr[i] in ans:
#         ans.append(arr[i])
# print(len(ans))

