# 세 정수가 입력되었을 때, 짝(even)/홀(odd)을 출력

a, b, c = map(int, input().split())
print('even' if a%2==0 else 'odd')
print('even' if b%2==0 else 'odd')
print('even' if c%2==0 else 'odd')
