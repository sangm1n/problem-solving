"""
추첨 조작
"""

from collections import deque

N = int(input())
ball = deque(map(int, input().split()))
letuin = list(map(int, input().split()))
tmp = letuin.copy()

result = []
while ball:
    left, right = ball[0], ball[-1]

    for i in range(len(letuin)):
        if tmp[i] == left:
            result.append(tmp[i])
            tmp.remove(tmp[i])
            ball.popleft()
            break
        if tmp[i] == right:
            result.append(tmp[i])
            tmp.remove(tmp[i])
            ball.pop()
            break

count = 0
for i in range(len(result)):
    if result[i] == letuin[i]:
        count += 1

if count == N:
    print(1)
elif count == N-1:
    print(2)
elif count == N-2:
    print(3)
else:
    print('ggwang')
print(*result)
