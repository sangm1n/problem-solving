"""
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = {input().rstrip() for _ in range(N)}
arr2 = {input().rstrip() for _ in range(M)}

result = list(arr1.intersection(arr2))

print(len(result))
[print(name) for name in result]
