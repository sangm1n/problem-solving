# 정수 순서대로 입력 (단, 개수는 알 수 없음)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력 중단
# 입력 : 7 4 2 3 0 1 5 6 9 10 8
# 출력 : 7
#        4
#        2
#        3

var = list(map(int, input().split()))
for i in var:
    if i==0: exit()
    else: print(i)
