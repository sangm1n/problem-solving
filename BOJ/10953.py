# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# A와 B는 콤마로 구분

n = int(input())

for i in range(n):
    a, b= map(int, input().split(','))
    print(a+b)