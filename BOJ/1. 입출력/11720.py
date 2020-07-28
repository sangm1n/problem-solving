# N개의 숫자를 공백 없이 입력해 합 출력

n = int(input())
num = input()
sum = 0
for i in range(n):
    sum += int(num[i])
print(sum)