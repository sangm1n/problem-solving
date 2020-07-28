"""
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다.
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
수빈이가 지금 이동하려고 하는 채널은 N이다.
어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
수빈이가 지금 보고 있는 채널은 100번이다.
"""

n = int(input())
num = int(input())
arr = set(str(x) for x in range(10))
if num==0:
    pass
else:
    error = set(input().split())
    arr = arr-error

result = abs(n - 100)
for i in range(1000001):
    boolean = True
    for a in str(i):
        if a not in arr:
            boolean = False
            break
    if boolean is True:
        result = min(result, abs(n-i) + len(str(i)))

print(result)