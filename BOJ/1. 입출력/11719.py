# 입력 받은 대로 출력

while True:
    try:
        print(input())
    except EOFError:
        break