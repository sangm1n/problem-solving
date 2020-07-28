# 나비넥타이 모양 별 찍기

n = int(input())
for i in range(1, n+1):
    print(('*'*i).ljust(n), ('*'*i).rjust(n), sep='')
for i in range(n-1, 0, -1):
    print(('*'*i).ljust(n), ('*'*i).rjust(n), sep='')