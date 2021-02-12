"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 신나는 함수 실행
description : Dynamic Programming
"""


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if not dp[a][b][c]:
            dp[a][b][c] = w(20, 20, 20)
        return dp[a][b][c]

    if a < b < c:
        if not dp[a][b][c]:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        if not dp[a][b][c]:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


arr = []
while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    arr.append([a, b, c])

maximum = 0
for i in range(len(arr)):
    maximum = max(maximum, max(arr[i]))

dp = [[[0 for _ in range(maximum+1)] for _ in range(maximum+1)] for _ in range(maximum+1)]

for a, b, c in arr:
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
