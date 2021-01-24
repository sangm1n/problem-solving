"""
다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
"""

def game(first, second):
    arr = ['가위', '바위', '보']

    if first == arr[0]:
        if second == arr[1]:
            print(arr[1] + '가 이겼습니다!')
        elif second == arr[2]:
            print(arr[0] + '가 이겼습니다!')
        else:
            print('비겼습니다!')
    elif first == arr[1]:
        if second == arr[0]:
            print(arr[1] + '가 이겼습니다!')
        elif second == arr[2]:
            print(arr[2] + '가 이겼습니다!')
        else:
            print('비겼습니다!')
    else:
        if second == arr[0]:
            print(arr[0] + '가 이겼습니다!')
        elif second == arr[1]:
            print(arr[1] + '가 이겼습니다!')
        else:
            print('비겼습니다!')


name1 = input()
name2 = input()
g1 = input()
g2 = input()

game(g1, g2)