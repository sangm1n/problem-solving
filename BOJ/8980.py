"""
아래 그림과 같이 직선 도로상에 왼쪽부터 오른쪽으로 1번부터 차례대로 번호가 붙여진 마을들이 있다.
마을에 있는 물건을 배송하기 위한 트럭 한 대가 있고, 트럭이 있는 본부는 1번 마을 왼쪽에 있다.
이 트럭은 본부에서 출발하여 1번 마을부터 마지막 마을까지 오른쪽으로 가면서 마을에 있는 물건을 배송한다.

각 마을은 배송할 물건들을 박스에 넣어 보내며, 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
박스들은 모두 크기가 같다. 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 있다.
이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송하려고 한다.

    - 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
    - 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
    - 조건 3: 박스들 중 일부만 배송할 수도 있다.

마을의 개수, 트럭의 용량, 박스 정보(보내는 마을 번호, 받는 마을번호, 박스 개수)가 주어질 때,
트럭 한 대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오. 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.
"""

import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

deliver = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
deliver.sort(key=lambda x: (x[1], x[0]))

village = [C] * (N + 1)
total = 0
for i in range(len(deliver)):
    start, end = deliver[i][0], deliver[i][1]
    box = deliver[i][2]
    max_capacity = min(village[start:end])

    if max_capacity == 0:
        continue

    if box <= max_capacity:
        for k in range(start, end):
            village[k] -= box
        total += box
    else:
        for k in range(start, end):
            village[k] -= max_capacity
        total += max_capacity

print(total)
