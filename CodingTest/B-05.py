"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 정렬된 두 리스트 합집합
"""

N, M = 3, 4
A = [1, 3, 5]
B = [2, 4, 6, 8]

result = [0] * (N+M)
i, j, k = 0, 0, 0

while i < N or j < M:
    if j >= M or (i < N and A[i] <= B[j]):
        result[k] = A[i]
        i += 1
    else:
        result[k] = B[j]
        j += 1
    k += 1

print(*result)
