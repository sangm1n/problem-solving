# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 출력

n = int(input())
for i in range(n):
    print('*'*(i+1))