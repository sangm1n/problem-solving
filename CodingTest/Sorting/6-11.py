"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 성적이 낮은 순서로 학생 출력하기
description : N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
"""
N = int(input())
score = []

for _ in range(N):
    name, num = map(str, input().split())
    score.append((name, int(num)))

result = sorted(score, key=lambda x: x[1])

for i in range(len(result)):
    print(result[i][0], end=' ')
