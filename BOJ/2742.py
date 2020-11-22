# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력 (역순)

n = int(input())
i = 0
for i in range(n, 0, -1):
    print(i)