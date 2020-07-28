# 10진수를 입력받아 16진수로 출력하는데, 대문자로 출력

var = int(input())
hexa = hex(var)[2:]
print(hexa.upper())