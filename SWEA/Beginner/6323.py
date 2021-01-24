"""
다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
"""

def fibonacci(number):
    arr = [1, 1]
    for i in range(2, number):
        arr.append(arr[i-2] + arr[i-1])

    return arr

n = int(input())
print(fibonacci(n))
