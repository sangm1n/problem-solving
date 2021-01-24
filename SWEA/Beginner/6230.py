"""
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
"""

score = [88, 30, 61, 55, 95]

for i in range(len(score)):
    if score[i] >= 60:
        print('{}번 학생은 {}점으로 합격입니다.'.format(i+1, score[i]))
    else:
        print('{}번 학생은 {}점으로 불합격입니다.'.format(i + 1, score[i]))
