# 2개의 참 또는 거짓이 입력될 때, 참/거짓이 서로 같을 때에만 참 출력

a, b = map(int, input().split())
print( (a and b) or ((not a) and (not b)) )