"""
There are pizza boxes all of which have the same dimensions.
The boxes are stacked in piles, forming a three- dimensional grid where the heights are all different.
The view from front shows the height of the tallest pile in each column, the view from the side shows the height of the tallest pile in each row.

What is the maximum number of pizza boxes we can remove without changing the front and side views?
In the following example, Figure I.2 shows the solution of Figure I.1(a) case.
In Figure I.1(a) and Figure I.2, each number (height) represents the number of boxes stacked.

Your task is to compute the maximum number of pizza boxes that can be removed without changing the original front and side views.
"""

import sys

N, M = map(int, sys.stdin.readline().split())
total = 0
pizza = []
count = set()

for i in range(N):
    pizza.append(list(map(int, sys.stdin.readline().split())))
    count.add(max(pizza[i]))
    total += sum(pizza[i])

for j in range(M):
    count.add(max(pizza[i][j] for i in range(N)))

print(total - sum(count))
