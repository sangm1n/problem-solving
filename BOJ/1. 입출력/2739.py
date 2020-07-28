# N을 입력받아 구구단 N단 출력

n = int(input())
for i in range(1, 9):
    print(n, '*', i, '=', n*i)