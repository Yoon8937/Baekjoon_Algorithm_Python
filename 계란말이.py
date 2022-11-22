def method(idx):
    if(idx==0):
        return 0
    elif(idx==1):
        return 1
    else:
        return method(idx-1) + method(idx-2)


num = 5
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,num+1):
#     for j in range(num,i,-1):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()
# print("hello")


