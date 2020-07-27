# 두 수를 입력받아 a와 b가 같으면 1, 같지 않으면 0 출력

a, b = map(int, input().split())
if (a == b):
    print(1)
elif (a != b):
    print(0)