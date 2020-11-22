# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성

week = ['SUM', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

a, b = map(int, input().split())
for i in range(a-1):
    day += month[i]
day = (day+b)%7

print(week[day])
