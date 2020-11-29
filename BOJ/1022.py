"""
크기가 무한인 정사각형 모눈종이가 있다. 모눈종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.
이 모눈종이 전체를 양의 정수의 소용돌이 모양으로 채울 것이다. 일단 숫자 1을 0행 0열에 쓴다.
그리고 나서 0행 1열에 숫자 2를 쓴다. 거기서 부터 소용돌이는 반시계 방향으로 시작된다. 다음 숫자는 다음과 같이 채우면 된다.
이 문제는 위와 같이 채운 것을 예쁘게 출력하면 된다. r1, c1, r2, c2가 입력으로 주어진다. r1, c1은 가장 왼쪽 위 칸이고, r2, c2는 가장 오른쪽 아래 칸이다.
예쁘게 출력한다는 것은 다음과 같이 출력하는 것이다.

    1. 출력은 r1행부터 r2행까지 차례대로 출력한다.
    2. 각 원소는 공백으로 구분한다.
    3. 모든 행은 같은 길이를 가져야 한다.
    4. 공백의 길이는 최소로 해야 한다.
    5. 모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 한다.
    6. 만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.
"""


def get_value(x, y):
    idx = max(abs(x), abs(y))
    before_base = (2 * (idx - 1) + 1) ** 2
    base = (2 * idx + 1) ** 2
    dx, dy = idx - x, idx - y

    if x >= y:
        return base - dx - dy
    else:

        return before_base + dx + dy


r1, c1, r2, c2 = map(int, input().split())

arr = []
for i in range(r1, r2 + 1):
    tmp = []
    for j in range(c1, c2 + 1):
        tmp.append(get_value(i, j))
    arr.append(tmp)

max_value = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        max_value = max(max_value, arr[i][j])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sub = len(str(max_value)) - len(str(arr[i][j]))
        if sub > 0:
            print(' ' * sub, end='')
        print(arr[i][j], end=' ')
    print('')
