# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제 (오른쪽 정렬)

n = int(input())
for i in range(n, 0, -1):
    print(('*'*i).rjust(n))