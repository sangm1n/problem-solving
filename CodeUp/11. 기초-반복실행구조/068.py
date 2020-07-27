# 영문자(a~z) 1개가 입력되었을 때, 그 문자까지의 알파벳 출력

var = ord(input())
for i in range(ord('a'), var+1, 1):
    print(chr(i), end=' ')

# tip : print 파라미터의 end는 줄바꿈을 없애줄 수 있음