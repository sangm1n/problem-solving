"""
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
123
234
345
그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
"""

num = int(input())
for k in range(num):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    x = y = 0
    result = arr[0][0]
    while True:
        if x == n-1 and y == n-1:
            break

        if y == n-1:
            x += 1
            result += arr[x][y]
        elif x == n-1:
            y += 1
            result += arr[x][y]
        elif arr[x][y+1] < arr[x+1][y]:
            y += 1
            result += arr[x][y]
        elif arr[x][y+1] > arr[x+1][y]:
            x += 1
            result += arr[x][y]
        else:
            if x == n-2:
                if y == n-2:
                    x += 1
                    result += arr[x][y]
                else:
                    y += 1
                    result += arr[x][y]
            else:
                if arr[x][y+2] <= arr[x+2][y]:
                    if arr[x][y+2] < arr[x+1][y+1]:
                        y += 1
                        result += arr[x][y]
                    else:
                        x += 1
                        result += arr[x][y]

    print('#{} {}'.format(k+1, result))


