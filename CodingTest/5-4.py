"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 재귀 함수 종료
"""
def recursive_function(i):
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수 호출')
    recursive_function(i+1)
    print(i, '번째 재귀 함수 종료')


recursive_function(1)