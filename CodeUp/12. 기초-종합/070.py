# 정수 1개를 입력받아 짝수 합 구하기

var = int(input())
sum = 0
for i in range(0, var, 2):
    sum+=i
print(sum)