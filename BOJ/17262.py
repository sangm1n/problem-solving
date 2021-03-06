"""
선물 포장 공장을 말아먹은 욱제는 계곡에서 백숙을 파느라 학교에 자주 가지 못한다. 하지만 월클의 인생은 피곤한 법!
욱제는 지금처럼 힘든 시기에도 자신을 기다리는 5조5억명의 열렬한 팬들을 위해 가끔씩 학교에 가 줘야 한다.
욱제는 백숙이 끓는 걸 지켜봐야 해서 가게를 오래 비울 수 없다.
그래서 욱제는 한 번 학교에 간 뒤 최소 시간동안 머물다가 모든 팬들과 한 번씩 인사를 하고 학교를 떠나려고 한다.

욱제는 임의의 시각에 학교에 오거나 학교를 떠날 수 있고, 단 한 번의 왕복만 한다. 동시에 여러 팬들에게 인사를 끝낼 수도 있다.
욱제는 잘생겨서 인사하면 팬들이 심쿵사로 바로 쓰러지기 때문에 인사를 하는데 소요되는 시간은 0이라고 하자.

백숙집 주방 이모 효빈이는 N명의 팬들이 학교에 머무르는 시간 [s, e]들을 몰래 조사했다.
효빈이는 욱제가 학교에 머무르는 시간을 계산해서 그 시간동안 땡땡이를 치기로 했다.
효빈이와 함께 욱제가 학교에 머무르는 최소의 시간을 계산해 보자!
"""

import sys

N = int(sys.stdin.readline())
fans = []
for i in range(N):
    fans.append(list(map(int, sys.stdin.readline().split())))

go_school = max(fans[i][0] for i in range(N))
go_home = min(fans[i][1] for i in range(N))

result = go_school - go_home

if result <= 0:
    print(0)
else:
    print(result)
