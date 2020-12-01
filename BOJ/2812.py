"""
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
"""

N, K = map(int, input().split())
number = list(input())

tmp = []
idx = K
for num in number:
    while tmp and idx > 0 and tmp[-1] < num:
        del tmp[-1]
        idx -= 1
    tmp.append(num)

print(''.join(tmp[:N-K]))
