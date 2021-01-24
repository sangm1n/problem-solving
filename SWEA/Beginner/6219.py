"""
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
(단, 약수가 2개일 경우 소수임을 나타내십시오)
"""

n = int(input())
count = 0
arr = []
for i in range(1, n+1):
    if n%i == 0:
        print('{}(은)는 {}의 약수입니다.'.format(i, n))
        count += 1
        arr.append(i)

if count == 2:
    print('{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.'.format(n, arr[0], arr[1]))