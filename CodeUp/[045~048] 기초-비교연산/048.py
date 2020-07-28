# 두 수를 입력받아 a와 b가 서로 다르면 1, 그렇지 않으면 0 출력

a, b = map(int, input().split())
if (a != b):
    print(1)
else:
    print(0)