### 너무 복잡하게 생각했었음...
s = input()
t = input()

if len(s) > len(t):
    s = s*2
    tmp = len(s) // len(t) + 1
    t = t*tmp
    t = t[:len(s)]
elif len(s) < len(t):
    t = t*2
    tmp = len(t) // len(s) + 1
    s = s * tmp
    s = s[:len(t)]

if s == t:
    print(1)
else:
    print(0)


### 더 나은 풀이(다른 사람)
a=input()
b=input()
if a*len(b)==b*len(a):
    print(1)
else:
    print(0)