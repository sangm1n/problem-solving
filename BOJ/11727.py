# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성

n = int(input())
arr = [0, 1, 3]

for i in range(3, n+1):
    next = arr[i-1] + arr[i-2]*2
    arr.append(next)
print(arr[n]%10007)