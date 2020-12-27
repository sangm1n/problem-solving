"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 순열과 조합
"""

from itertools import permutations
from itertools import combinations

data = [1, 2, 3]

p = list(permutations(data, 2))
c = list(combinations(data, 2))

print(p)
print(c)
