length, money= map(int,input().split())
arr=[]
# money= 55000
# arr = [1,5,10,50,100,500,1000,5000,10000,50000]
for i in range(length):
    num = int(input())
    arr.append(num)
arr.reverse() #가장 큰 수부터 나누어야 됨으로, 가장 큰수부터 시작하도록 배열을 뒤집어줌.
cnt = 0
for i in arr:
    if i <= money:# =을 빼먹어서 틀리게 나왔음.
        cnt += money//i
        money = money%i
print(cnt)


### 처음에 풀었던 방식(시간 초과됨).  while문 for문을 두번사용함
# arr = [1,5,10,50,100,500,1000,5000,10000,50000]
# money = 4790
# # money = 55000 #if문을 타지 않음.
# cnt = 0
# maxx = max(arr)#만약 money=51000일때, 배열안에 money보다 큰수가 없으니까, max(arr)로 선언해놓음. 그러면은 if문을 실행 안시킴.
# while True:
#     for i in range(len(arr)):
#         if arr[i] > money: #배열에서 돈보다 바로 큰것에서. ex)money=1000, arr[i]=5000
#             maxx = arr[i-1]#바로 큰것보다 전에것. 즉, ex)5000원의 i-1, 1000원이 선택됨.
#             break
#     print("사용된 것: "+str(maxx))
#
#     if money-maxx >=0:
#         money -=maxx
#         cnt +=1
#         if money==0:
#             break
# print("cnt : "+str(cnt))