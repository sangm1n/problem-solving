"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""

N = int(input())

for i in range(N):
    print(' ' * (N-i-1), end='')
    print('*', end='')

    if i == 0:
        print('')
        continue

    print(' ' * (2*i-1), end='')
    print('*')
