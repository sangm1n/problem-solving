"""
다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
"""

game = ['가위', '바위', '보']
m1 = input()
m2 = input()

if m1 == '가위':
    if m2 == '바위':
        print('Result : Man2 Win!')
    elif m2 == '보':
        print('Result : Man1 Win!')
    else: print('Result : Draw')
elif m1 == '바위':
    if m2 == '가위':
        print('Result : Man1 Win!')
    elif m2 == '보':
        print('Result : Man2 Win!')
    else: print('Result : Draw')
else:
    if m2 == '바위':
        print('Result : Man1 Win!')
    elif m2 == '가위':
        print('Result : Man2 Win!')
    else: print('Result : Draw')