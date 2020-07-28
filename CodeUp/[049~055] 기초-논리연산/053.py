# 2가지 참 또는 거짓이 입력될 때, 참/거짓이 서로 다를 때에만 참 출력

a, b = map(int, input().split())
print( (a and (not b) or ((not a) and b)) )

# tip : a XOR b
#       (  (a AND (NOT b)) OR ((NOT a) AND b)  )