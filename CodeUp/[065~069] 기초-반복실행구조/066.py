# n개의 정수를 입력하여 순서대로 출력
# 첫 줄에 정수의 개수 n이 입력되고, 두번째 줄에 n개의 정수 공백을 두고 입력

n = int(input())
var = list(map(int, input().split()))
for i in range(len(var)):
    print(var[i])