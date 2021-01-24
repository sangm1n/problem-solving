"""
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
"""

num = [int(input()) for x in range(5)]

print('입력된 값 {}의 평균은 {}입니다.'.format(num, sum(num)/len(num)))