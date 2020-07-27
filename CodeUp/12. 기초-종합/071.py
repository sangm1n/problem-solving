# 원하는 문자(q)가 입력될 때까지 반복 출력

arr = list(input().split())
for i in arr:
    print(i)
    if i=='q': break;