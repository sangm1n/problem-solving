# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 출력 시 "Case #x: A + B = C" 형식으로 출력

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))
