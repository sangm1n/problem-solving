# 5자리 정수 1개를 입력받아 각 자리별로 나누어 출력
# 입력 : 75254
# 출력 : [70000]
#        [5000]
#        [200]
#        [50]
#        [4]

var = input()
count = len(var) - 1
for i in range(len(var)):
    print([int(var[i] + '0'*count)])
    count -= 1
