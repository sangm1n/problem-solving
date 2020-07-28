# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제 (피라미드 모양)

n = int(input())
for i in range(1, n+1):
    print(' '*(n-i), '*'*(2*i-1), sep='')