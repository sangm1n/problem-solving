# 모래시계 모양 별 찍기

n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i), '*'*(2*i-1), sep='')
for i in range(2, n+1):
    print(' '*(n-i), '*'*(2*i-1), sep='')