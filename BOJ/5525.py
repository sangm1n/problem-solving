"""
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

- P1 IOI
- P2 IOIOI
- P3 IOIOIOI
- PN IOIOI...OI (O가 N개)

I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
"""

N = int(input())
M = int(input())
S = input()

count = 0
pattern = 0

idx = 1
while idx < M-1:
    value = S[idx-1:idx+2]

    if value == 'IOI':
        pattern += 1
        if pattern == N:
            count += 1
            pattern -= 1
        idx += 1
    else:
        pattern = 0
    idx += 1

print(count)
