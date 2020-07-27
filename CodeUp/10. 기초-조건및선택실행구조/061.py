# 정수 1개가 입력되었을 때, 음/양과 짝/홀을 출력

var = int(input())
print('minus' if var<0 else 'plus')
print('even' if var%2==0 else 'odd')