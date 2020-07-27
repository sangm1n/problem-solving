# 단어를 하나 입력받아 한 문자씩 분리해 출력 ('' 로 묶어 출력)
# 입력 : 'Boy'
# 출력 : 'B'
#        'o'
#        'y'

var = input()
for i in range(len(var)):
    print("'{}'".format(var[i]))