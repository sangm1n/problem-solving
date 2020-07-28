# 별 찍기 (특수한 피라미드 모양)

n = int(input())
for i in range(1, n+1):
    print(' '*(n-i), '* '*i, sep='')