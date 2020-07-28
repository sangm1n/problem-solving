# 입력된 세 정수 중 가장 작은 값 출력 (삼항연산자 사용)

a, b, c = map(int, input().split())
min = a < b and a or b
print(min < c and min or c)

# min = a if a < b else b
# print(min if min < c else c)