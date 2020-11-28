"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""

N = int(input())

for i in range(1, N):
    last = (N-i) * 4 + 1
    print('* ' * (i-1) + '*' * last + ' *' * (i-1))
    print('* ' * i + ' ' * (last - 4) + ' *' * i)
print('* ' * (N * 2 - 1))
for i in range(N-1, 0, -1):
    last = (N-i) * 4 + 1
    print('* ' * i + ' ' * (last - 4) + ' *' * i)
    print('* ' * (i-1) + '*' * last + ' *' * (i-1))
