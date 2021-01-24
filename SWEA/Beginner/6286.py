"""
리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
"""

result = [1, 1]
[result.append(result[x-1] + result[x-2]) for x in range(2, 10)]
print(result)