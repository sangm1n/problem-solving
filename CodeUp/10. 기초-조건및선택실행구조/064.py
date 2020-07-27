# 월이 입력될 때 계절 이름 출력
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall
# 12, 1, 2 : winter

var = int(input())
if var==3 or var==4 or var==5: print('spring')
elif var==6 or var==7 or var==8: print('summer')
elif var==9 or var==10 or var==11: print('fall')
else: print('winter')