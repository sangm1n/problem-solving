"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자 카드 게임
description : 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.
    - 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다.
    - 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
    - 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
    - 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
"""

N, M = map(int, input().split())

result = 0
for i in range(N):
    arr = list(map(int, input().split()))
    min_value = min(arr)
    result = max(min_value, result)

print(result)
