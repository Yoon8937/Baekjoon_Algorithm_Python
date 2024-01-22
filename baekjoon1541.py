# 처음 문제를 읽고 풀 땐, 괄호를 한번만 사용하는 줄 암,
# 그래서 틀림. 문제에서 괄호의 갯수에 대해 제한하지는 않았음.
exp = input()
nums = []
exp += 'e'
sidx = 0
idx = 0
while True:
    if exp[idx] == 'e':
        nums.append(int(exp[sidx:idx]))
        break

    if exp[idx+1] == '-' or exp[idx+1] == '+':
        nums.append(int(exp[sidx:idx+1]))
        print(exp[sidx:idx+1])
        sidx = idx+1
    idx += 1

answer = sum(nums)
nums.append(0)
for i in range(len(nums)-1):
    if nums[i] < 0:
        k = i
        while True:
            if nums[k] >=0:
                answer -= (nums[k]*2)
            if nums[k+1] < 0 or k+1==len(nums)-1:
                break
            k +=1
print(answer)











# input().split('-')문법을 잘 사용하지 못 했음...생각은 했으나...
exp = input().split('-')
# print(exp)

answer = 0
def method(expp:str)->int:
    tmp = expp.split('+')
    return sum(map(int,tmp))

for i in range(len(exp)):
    num = method(exp[i])
    if i == 0:
        answer = num
    else:
        answer -= num
print(answer)









### 더 나은 풀이(다른 사람)
exp = input().split('-')
num = []
for i in exp:
    cnt = 0
    sum = i.split('+')
    for j in sum:
        cnt += int(j)
    num.append(cnt)
ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)
