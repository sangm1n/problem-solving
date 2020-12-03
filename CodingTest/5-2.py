"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Queue
"""

from collections import deque

queue = deque()

# 5 삽입 -> 2 삽입 -> 3 삽입 -> 7 삽입 -> 삭제 -> 1 삽입 -> 4 삽입 -> 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

queue = list(queue)
print(queue)
print(queue[::-1])
