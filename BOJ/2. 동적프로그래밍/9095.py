# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성

n = int(input())
arr = [0, 1, 2, 4]

for i in range(4, 11):
    sum = arr[i-1] + arr[i-2] + arr[i-3]
    arr.append(sum)

for i in range(n):
    num = int(input())
    print(arr[num])