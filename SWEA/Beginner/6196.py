"""
1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.
"""

n = input()
sum = int(n) + int(n*2) + int(n*3) + int(n*4)
print(sum)