"""
끊어진 수도관
"""

N, M = map(int, input().split())

bundle, piece = [], []
for _ in range(M):
    four, one = map(int, input().split())
    bundle.append(four)
    piece.append(one)

min_bundle = min(bundle)
min_piece = min(piece)

quotient, rest = N // 4, N % 4
result = 0
if 4 * min_piece < min_bundle:
    result = min_piece * N
elif rest * min_piece > min_bundle:
    result = min_bundle * (quotient + 1)
else:
    result = min_bundle * quotient + min_piece * rest

print(result)
