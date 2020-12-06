"""
남규는 통나무를 세워 놓고 건너뛰기를 좋아한다. 그래서 N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다.
남규는 원형으로 인접한 옆 통나무로 건너뛰는데, 이때 각 인접한 통나무의 높이 차가 최소가 되게 하려 한다.

통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다. 높이가 {2, 4, 5, 7, 9}인 통나무들을 세우려 한다고 가정하자.
이를 [2, 9, 7, 4, 5]의 순서로 세웠다면, 가장 첫 통나무와 가장 마지막 통나무 역시 인접해 있다.
즉, 높이가 2인 것과 높이가 5인 것도 서로 인접해 있다. 배열 [2, 9, 7, 4, 5]의 난이도는 |2-9| = 7이다.
우리는 더 나은 배열 [2, 5, 9, 7, 4]를 만들 수 있으며 이 배열의 난이도는 |5-9| = 4이다.
이 배열보다 난이도가 낮은 배열은 만들 수 없으므로 이 배열이 남규가 찾는 답이 된다.
"""

import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    logs = list(map(int, sys.stdin.readline().split()))

    logs = deque(sorted(logs))
    result = [0] * N
    flag = True

    start, end = 0, N-1
    while logs:
        if flag:
            result[start] = logs.popleft()
            start += 1
            flag = False
        else:
            result[end] = logs.popleft()
            end -= 1
            flag = True

    gap = max(abs(result[j-1] - result[j]) for j in range(1, N))

    print(gap)
