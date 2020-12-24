"""

"""

N = int(input())
pos = list(map(int, input().split()))

pos.sort()

min_dist = 1e9
answer = 0
for i in range(len(pos)):
    antena = pos[i]
    result = 0
    for j in range(len(pos)):
        result += abs(pos[j] - pos[i])

    if result < min_dist:
        min_dist = result
        answer = i
    elif result == min_dist:
        min_dist = result

print(pos[answer])
