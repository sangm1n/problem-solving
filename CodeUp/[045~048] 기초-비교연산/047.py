# 두 수를 입력받아 b가 a보다 크거나 같으면 1, 그렇지 않으면 0 출력

a, b = map(int, input().split())
if (b >= a):
    print(1)
else:
    print(0)