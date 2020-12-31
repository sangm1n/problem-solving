"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 회전하는 큐
description : Deque
"""

from collections import deque

N, M = map(int, input().split())
compare = list(map(int, input().split()))

arr = list(range(1, N+1))
q = deque(arr)

result = 0
for num in compare:
    if num == q[0]:
        q.popleft()
    else:
        idx = q.index(num)
        if idx > len(q) // 2:
            while q[0] != num:
                q.appendleft(q.pop())
                result += 1
        else:
            while q[0] != num:
                q.append(q.popleft())
                result += 1
        q.popleft()

print(result)
