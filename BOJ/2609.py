"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

import sys
import math

N, M = map(int, sys.stdin.readline().split())

print(math.gcd(N, M))
print(N * M // math.gcd(N, M))
