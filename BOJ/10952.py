# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 마지막 입력은 0 0

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)