import sys

arr = sys.stdin.read().splitlines()
for i in range(len(arr)):
    a = int(arr[i].split()[0])
    b = int(arr[i].split()[1])
    c = int(arr[i].split()[2])

    print(max(b - a - 1, c - b - 1))

### 더 나은 풀이(다른 사람)
while True:
    try:
        a, b, c = map(int, input().split())
        result = max(b - a, c - b)
        print(result - 1)
    except:  # 아무것도 입력하지 않으면 except문을 타서 종료됨.
        break

import sys

while True:
    # input_data = sys.stdin.readline().rstrip()
    input_data = sys.stdin.readline()[:-1]
    if not input_data:
        break
    a, b, c = map(int, input_data.split())
    print(max(b - a, c - b) - 1)


