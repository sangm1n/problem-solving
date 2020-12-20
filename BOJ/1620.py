"""
그럼 다솜아 이제 진정한 포켓몬 마스터가 되기 위해 도감을 완성시키도록 하여라.
일단 네가 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나,
포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록 하여라. 나의 시험을 통과하면, 내가 새로 만든 도감을 주도록 하겠네.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
digit = dict()
alpha = dict()

for i in range(1, N+1):
    name = input().rstrip()
    digit[i] = name
    alpha[name] = i

for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(digit[int(question)])
    else:
        print(alpha[question])
