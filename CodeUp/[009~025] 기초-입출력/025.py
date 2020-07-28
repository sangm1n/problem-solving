# 년원일(yyyy.mm.dd)를 입력받아 일월년(dd-mm-yyyy)로 출력
# 한 자리 일/월은 0을 붙여 두자리로 출력

y, m, d = input().split('.')
if (len(m) == 1):
    m = '0' + m
if (len(d) == 1):
    d = '0' + d

print('{}-{}-{}'.format(d, m, y))

# tip : 삼항연산자 이용
#       m = '0' + m if len(m) == 1 else m
#       d = '0' + d if len(d) == 1 else d