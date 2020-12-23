"""
영식이와 친구들이 원형으로 모여서 시계방향으로 1부터 N까지 적혀있는 자리에 앉는다.
영식이와 친구들은 공 던지는 게임을 하기로 했다. 게임의 규칙은 다음과 같다.

일단 1번 자리에 앉은 사람이 공을 받는다. 그리고 나서 공을 다른 사람에게 던진다.
다시 공을 받은 사람은 다시 공을 던지고, 이를 계속 반복한다. 한 사람이 공을 M번 받았으면 게임은 끝난다. (지금 받은 공도 포함하여 센다.)
공을 M번보다 적게 받은 사람이 공을 던질 때, 현재 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게, 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다.

공을 총 몇 번 던지는지 구하는 프로그램을 작성하시오.
"""

N, M, L = map(int, input().split())

people = [x for x in range(1, N+1)]
get_ball = [0 for x in range(N)]

idx = 0
get_ball[idx] = 1

count = 0
while True:
    if get_ball[idx] == M:
        break

    if get_ball[idx] % 2 == 1:
        idx = (idx + L) % N
    else:
        idx = (idx - L) % N

    get_ball[idx] += 1
    count += 1

print(count)
