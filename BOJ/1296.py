"""
오민식은 자기가 좋아하는 여자 N명 중에 한 명과 함께 데이트하러 나가고 싶어한다.
하지만 N명 모두를 사랑하는 오민식에게는 한 명을 선택하고 나머지 여자를 버리는 것은 슬픈 결정이기 때문에 누구를 선택해야 할지 고민에 빠졌다.
마침 오민식은 사랑계산기를 얻었다. 사랑계산기는 두 사람의 이름을 이용해서 두 사람이 성공할 확률을 계산해 준다. 사랑계산기는 다음과 같이 작동한다.

    L = 두 사람 이름에서 등장하는 L의 개수
    O = 두 사람 이름에서 등장하는 O의 개수
    V = 두 사람 이름에서 등장하는 V의 개수
    E = 두 사람 이름에서 등장하는 E의 개수

위의 개수를 모두 계산 한 후에 확률 계산은 다음과 같이 한다.

((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) mod 100

오민식의 영어 이름과 나머지 여자들의 이름이 주어졌을 때, 오민식과 성공할 확률이 가장 높은 여자의 이름을 출력하는 프로그램을 작성하시오.
여러명일 때에는 알파벳으로 가장 앞서는 이름을 출력하면 된다.
"""

name = input()
N = int(input())

result, girl = -1, ''
for i in range(N):
    girl_name = input()

    L = name.count('L') + girl_name.count('L')
    O = name.count('O') + girl_name.count('O')
    V = name.count('V') + girl_name.count('V')
    E = name.count('E') + girl_name.count('E')
    calc = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    if calc > result:
        result, girl = calc, girl_name
    elif calc == result:
        girl = min(girl, girl_name)

print(girl)
