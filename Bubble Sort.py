#####버블정렬(Bubble sort)#####

arr = [7, 4, 5, 1, 3]
for i in range(1,len(arr)):
    tmp=0
    for j in range(len(arr)-i):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
        print(arr)
    print()

print("result : "+str(arr))



####처음에는 이렇게함
# for j in range(len(arr),1,-1):
#     tmp=0
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             tmp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = tmp
#         print("arr={0}".format(arr))
#     print()
# print(arr)

