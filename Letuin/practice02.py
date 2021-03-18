"""
추첨 조작 : 해시 테이블
"""

N = int(input())
cylinder = list(map(int, input().split()))
tmp = list(map(int, input().split()))

if N == 1:
    if cylinder[0] == tmp[0]:
        print(1)
        print(tmp[0])
    else:
        print(2)
        print(tmp[0])
    exit()

letuin = [0] * (N+1)
for idx, val in enumerate(tmp):
    letuin[val] = idx+1

start, end = 0, N-1
result = []
while start <= end:
    left, right = cylinder[start], cylinder[end]

    if letuin[left] < letuin[right]:
        result.append(left)
        start += 1
    else:
        result.append(right)
        end -= 1

count = 0
for i in range(N):
    if result[i] == tmp[i]:
        count += 1

if count == N:
    print(1)
elif count == N-1:
    print(2)
elif count == N-2:
    print(3)
else:
    print("fail")
print(*result)
