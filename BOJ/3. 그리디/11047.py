# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성

a, b = map(int, input().split())
value = []
for _ in range(a):
    value.append(int(input()))

count = 0
for i in range(a-1, -1, -1):
    if b==0: break
    if b<value[i]:
        continue
    count += b//value[i]
    b = b%value[i]
print(count)
