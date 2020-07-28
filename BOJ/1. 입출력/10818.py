# N개의 정수가 주어졌을 때, 최솟값과 최댓값 출력

n = int(input())
num = list(map(int, input().split()))
num.sort()

print(num[0], num[-1])