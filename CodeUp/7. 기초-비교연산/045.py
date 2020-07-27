# 두 수를 입력받아 a가 b보다 크면 1, a가 b보다 작거나 같으면 0 출력

a, b = map(int, input().split())
if (a > b):
    print(1)
elif (a <= b):
    print(0)