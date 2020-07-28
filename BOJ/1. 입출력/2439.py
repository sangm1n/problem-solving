# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍기 (오른쪽 정렬)

n = int(input())
for i in range(1, n+1):
    print(('*'*i).rjust(n))