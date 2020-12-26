"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 부분 연속 수열 찾기
"""

N, M = 5, 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1

    if interval_sum == M:
        count += 1
    interval_sum -= data[start]

print(count)
