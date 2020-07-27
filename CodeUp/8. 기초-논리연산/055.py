# 2개의 참 또는 거짓이 입력될 때, 모두 거짓일 때에만 참 출력

a, b = map(int, input().split())
print( (not a) and (not b) )