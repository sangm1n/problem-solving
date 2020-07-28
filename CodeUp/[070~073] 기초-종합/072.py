# 1,2,3... 계속 더해 그 합이 입력한 정수보다 같거나 작을 때까지 계속 더하는 프로그램
# 마지막에 더한 정수 출력

var = int(input())
sum = 0
for i in range(1, var+1):
    sum+=i
    if sum>=var:
        print(i)
        break
