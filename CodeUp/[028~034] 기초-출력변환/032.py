# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력

var = '0x' + input()
ten = int(var, 16)
print(oct(ten)[2:])

# tip : 16진수 -> 10진수 -> 8진수 순서