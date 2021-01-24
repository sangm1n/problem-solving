"""
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
"""

n = input()
n = list(n)
count = [0 for x in range(10)]

for i in n:
    count[int(i)] += 1

arr = []
print('0 1 2 3 4 5 6 7 8 9')
for i in range(len(count)):
    if i == len(count)-1:
        print(count[i])
    else:
        print(count[i], end=' ')