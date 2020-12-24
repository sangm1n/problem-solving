"""

"""

N = int(input())
cards = [int(input()) for _ in range(N)]

cards.sort()
dp = [0] * (N+1)

if len(cards) <= 2:
    print(sum(cards))
else:
    dp[0] = cards[0] + cards[1]

    for i in range(1, len(cards) - 1):
        dp[i] = dp[i-1] + cards[i+1]

    print(sum(dp))
