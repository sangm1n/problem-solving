"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 커리큘럼
description : 온라인 강의는 선수 강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
예를 들어 '알고리즘' 강의의 선수 강의로 '자료구조'가 존재한다면, '자료구조'를 들은 이후에 '알고리즘' 강의를 들을 수 있다.
모든 강의는 1번부터 N번까지의 번호를 가지며 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
예를 들어 N=3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고, 1번과 2번 강의는 선수 강의가 없다고 가정하자.
각 강의에 대하여 강의 시간은 다음과 같다.
    - 1번 강의 : 30시간
    - 2번 강의 : 20시간
    - 3번 강의 : 40시간
이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간, 3번 강의를 수강하기까지의 최소 시간은 70시간이다.

N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.
"""

from collections import deque
import copy


def torpology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    [print(result[x]) for x in range(1, N+1)]


N = int(input())
indegree = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    time[i] = info[0]

    for x in info[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

torpology_sort()
