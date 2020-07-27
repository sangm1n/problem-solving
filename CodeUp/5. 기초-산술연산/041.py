# 정수 2개를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값 계산하여 한 줄씩 출력
# 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력

a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, round(a/b, 2), sep='\n')