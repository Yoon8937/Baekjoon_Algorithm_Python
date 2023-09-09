### 나의 풀이
n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([b,a])
arr.sort()
ans = []
tmp = 0
ftmp = 0
for i in range(n):
    if i==0:
        ans.append(arr[i])
        tmp = arr[i][1]
        ftmp = arr[i][0]
    elif tmp <= arr[i][1] and arr[i][1] >= ftmp:
        ans.append(arr[i])
        tmp = arr[i][1]
        ftmp = arr[i][0]
print(len(ans))


n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([b,a])
arr.sort()
tmp = 0
ftmp = 0
ans = 0
for i in range(n):
    if tmp <= arr[i][1] and arr[i][1] >= ftmp:
        ans += 1
        tmp = arr[i][1]
        ftmp = arr[i][0]
print(ans)



### 더 나은 풀이(다른 사람)
##########################################################################################
n = int(input())
room = []
for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])
room.sort(key = lambda x: x[0]) # 첫 번째로 인덱스로 정렬을 함
room.sort(key = lambda x: x[1]) # 첫 번째 인덱스를 기준으로 정렬한 기준에서 다시 두 번째 인덱스로 정렬을 함. 밑에 코드 참고하기.
# 아니면 한 줄로도 가능
# arr.sort(key = lambda x: (x[1], x[0])) #두 번째 요소(인덱스 1)를 기준으로 정렬 그리고 첫 번째 요소(인덱스 0)를 기준으로 정렬
# 즉, 두 번째 요소를 기준으로 오름차순으로 정렬하고, 두 번째 요소가 동일한 경우 첫 번째 요소를 기준으로 오름차순으로 정렬
print(room)
cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]
print(cnt)


# info1
arr = [[1, 3], [4, 4], [3, 4], [5, 8], [6, 8], [7, 8], [8, 8], [9, 10], [10, 10], [2, 2]]
print("Before sorting:")
print(arr)


arr.sort(key = lambda x: x[1])

print("After sorting by second index:")
print(arr)
# [[2, 2], [1, 3], [4, 4], [3, 4], [5, 8], [6, 8], [7, 8], [8, 8], [9, 10], [10, 10]]



print("===================================================================================")
arr = [[1, 3], [4, 4], [3, 4], [5, 8], [6, 8], [7, 8], [8, 8], [9, 10], [10, 10], [2, 2]]
print("Before sorting:")
print(arr)

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

print("After sorting by both first and second index:")
print(arr)
# [[2, 2], [1, 3], [3, 4], [4, 4], [5, 8], [6, 8], [7, 8], [8, 8], [9, 10], [10, 10]]


# info2
# 이중 리스트일 때, key에 lambda를 사용하여 정렬 기준을 설정할 수 있다.

# list[0]를 기준으로 정렬
arr = [[3, 'three'],[4, 'four'],[2, 'two'],[1, 'one']]
print(sorted(arr, key=lambda x : x[0]))
# arr.sort(key=lambda x : x[0]) 
# 출력 : [[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four']]


# 문자열의 길이를 기준으로 정렬
arr = ['my', 'i', 'love', 'dog']
# print(sorted(arr, key=lambda x : len(x)))
arr.sort(key=lambda x : len(x))
#출력 : ['i', 'my', 'dog', 'love']
##########################################################################################



# N, *ls = map(int, open(0).read().split())
# ls = sorted(zip(ls[::2], ls[1::2]))
#
# cnt = 0
# e = 0
# for i, j in ls:
#     if i >= e:
#         e = j
#         cnt += 1
#     else:
#         if j < e:
#             e = j
# print(cnt)