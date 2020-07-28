# 주사위를 2개 던져 1부터 n까지, 1부터 m까지 나올 수 있는 모든 경우 출력
# 입력 : 2 3
# 출력 : 1 1
#        1 2
#        1 3
#        2 1
#        2 2
#        2 3

a, b = map(int, input().split())
for a in range(1, a+1):
    for b in range(1, b+1):
        print(a, b)
