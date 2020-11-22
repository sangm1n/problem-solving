# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 각 줄에 A와 B가 주어짐

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break