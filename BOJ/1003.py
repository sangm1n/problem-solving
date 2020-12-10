"""
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

    - fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
    - fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
    - 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
    - fibonacci(0)은 0을 출력하고, 0을 리턴한다.
    - fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
    - 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
    - fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.

1은 2번 출력되고, 0은 1번 출력된다.
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def fibonacci(n):
    result = [(1, 0), (0, 1)]

    if n == 0:
        return result[0]
    elif n == 1:
        return result[1]
    else:
        for i in range(2, n+1):
            first = result[i-2][0] + result[i-1][0]
            second = result[i-2][1] + result[i-1][1]

            result.append((first, second))

        return result[n]


N = int(input())
for _ in range(N):
    num = int(input().rstrip())

    print(fibonacci(num)[0], fibonacci(num)[1])

