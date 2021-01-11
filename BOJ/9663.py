"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : N-Queen
description : Back-tracking
"""


def queen(arr):
    global count

    if len(arr) == N:
        count += 1
        return

    sub = list(range(N))
    for i in range(len(arr)):
        if arr[i] in sub:
            sub.remove(arr[i])
        dist = len(arr) - i

        if arr[i] + dist in sub:
            sub.remove(arr[i] + dist)
        if arr[i] - dist in sub:
            sub.remove(arr[i] - dist)

    if sub:
        for s in sub:
            arr.append(s)
            queen(arr)
            arr.pop()
    else:
        return


N = int(input())
count = 0

for i in range(N):
    queen([i])
print(count)
