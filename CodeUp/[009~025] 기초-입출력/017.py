# 년, 월, 일을 입력받아 지정된 형식으로 출력
# 입력 : 연, 월, 일이 . 으로 구분되어 입력
# 출력 : yyyy.mm.dd 형식으로 출력 (m 혹은 d가 한 자리 수인 경우 앞에 0 붙여 출력)

y, m, d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d = '0' + d

print('{}.{}.{}'.format(y, m, d))