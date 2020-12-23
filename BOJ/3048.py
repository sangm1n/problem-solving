"""
개미가 일렬로 이동할 때, 가장 앞의 개미를 제외한 나머지 개미는 모두 앞에 개미가 한 마리씩 있다.

서로 반대 방향으로 이동하던 두 개미 그룹이 좁은 길에서 만났을 때, 개미는 어떻게 지나갈까?

최근 연구에 의하면 위와 같은 상황이 벌어지면 개미는 서로를 점프해서 넘어간다고 한다.

즉, 두 그룹이 만났을 때, 1초에 한번씩 개미는 서로를 뛰어 넘는다. (한 개미가 다른 개미를 뛰어 넘고, 다른 개미는 그냥 전진한다고 생각해도 된다)

하지만 모든 개미가 점프를 하는 것은 아니다. 자신의 앞에 반대 방향으로 움직이던 개미가 있는 경우에만 점프를 하게 된다.

첫 번째 그룹이 ABC로 움직이고, 두 번째 그룹의 개미가 DEF순으로 움직인다고 하자. 그럼, 좁은 길에서 만났을 때, 개미의 순서는 CBADEF가 된다. 1초가 지났을 때는 자신의 앞에 반대방향으로 움직이는 개미가 있는 개미는 A와 D다. 따라서, 개미의 순서는 CBDAEF가 된다. 2초가 되었을 때, 자신의 앞에 반대 방향으로 움직이는 개미는 B,D,A,E가 있다. 따라서, 개미의 순서는 CDBEAF가 된다.

T초가 지난 후에 개미의 순서를 구하는 프로그램을 작성하시오.
"""

N, M = map(int, input().split())
g1 = list(map(str, input()))
g2 = list(map(str, input()))
g1 = g1[::-1]
ant = g1 + g2

T = int(input())

r_status = ['R' for _ in range(N)]
l_status = ['L' for _ in range(M)]
status = r_status + l_status

while T > 0:
    i = 0

    while i < len(ant):
        if i+1 < len(ant) and status[i] == 'R' and status[i+1] == 'L':
            status[i], status[i+1] = 'L', 'R'
            ant[i], ant[i+1] = ant[i+1], ant[i]

            i += 2
            continue
        i += 1
    T -= 1

print(''.join(ant))
