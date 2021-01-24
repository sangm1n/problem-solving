"""
100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
"""

arr = []
for i in range(100, 301):
    if i%2 == 0 and str(i)[0] not in '13579' and str(i)[1] not in '13579'\
            and str(i)[2] not in '13579':
        arr.append(str(i))

print(",".join(arr))