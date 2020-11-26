"""
정수 N이 주어져 있을 때 이 수가 10보다 크면 일의 자리에서 반올림을 하고,
이 결과가 100보다 크면 다시 10의 자리에서 반올림을 하고, 또 이 수가 1000보다 크면 100의 자리에서 반올림을 하고.. (이하 생략)
이러한 연산을 한 결과를 출력하시오.
"""

N = int(input())

start = 10
while N > start:
    temp = N % start

    if temp >= start // 2:
        N += start
    N -= temp
    start *= 10

print(N)
