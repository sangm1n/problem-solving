# 점수 (정수, 0~100)을 입력받아 평가 출력
# 90 ~ 100 : A
# 70 ~ 89  : B
# 40 ~ 69  : C
#  0 ~ 39  : D

var = int(input())
if var>=90: print('A')
elif var>=70: print('B')
elif var>=40: print('C')
else: print('D')