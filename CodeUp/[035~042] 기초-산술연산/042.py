# 정수 3개를 입력받아 합과 평균 한 줄씩 출력
# 소수점 이하 둘째 자리에서 반올림해 소수점 이하 첫째 자리까지 출력

a, b, c = map(int, input().split())
print(a+b+c, round((a+b+c)/3, 1), sep='\n')