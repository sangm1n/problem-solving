# 평가를 문자로 입력받아 내용을 다르게 출력
# A : best
# B : good
# C : run
# D : slowly
# 나머지 : what?

var = input()
if var=='A': print('best')
elif var=='B': print('good')
elif var=='C': print('run')
elif var=='D': print('slowly')
else: print('what?')