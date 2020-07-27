# 입력된 두 정수 중 큰 값 출력 (삼항연산자 사용)

a, b = map(int, input().split())
print(a > b and a or b)