"""
끊어진 수도관
"""

N, M = map(int, input().split())
bundle, piece = [], []

for _ in range(M):
    four, one = map(int, input().split())
    bundle.append(four)
    piece.append(one)

dp = [0 for _ in range(N+4)]
dp[1] = min(piece)
min_piece = min(piece)
min_bundle = min(bundle)

for i in range(2, N+4):
    if i < 4:
        dp[i] = min(piece) * i
    else:
        dp[i] = min(dp[i-1] + min_piece, dp[i-4] + min_bundle)

result = dp[N]
for i in range(N+1, N+4):
    result = min(result, dp[i])
print(result)
